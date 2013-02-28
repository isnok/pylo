#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" A wrapper for the jbofihe parser. """

from Helpers import run_jbofihe
from Helpers import sanitize_input

class LojbanParser:

    """ A wrapper for jbofihe. """

    def __init__(self, args):
        self.verbose = args.verbose

    def parse(self, inp):

        """ Parse the input given. """

        # old list of "interesting jbofihe args:"
        #parser_args = ('-bt -dd', '-ie', '-sev' '-t', '-x -b')

        if self.verbose:
            print "Input: %r" % inp

        string = sanitize_input(inp)

        if self.verbose:
            print 'Parsing: "%s"' % string.replace('\\','')

        xb_out = self.parse_xb(string)

        if self.verbose:
            print "Output of 'jbofihe -x -b':"
            for i in xb_out:
                print i

        t_out = self.parse_t(string)
        if self.verbose > 1:
            def out_t(tree, indent=""):
                fmt = ""
                for n in tree:
                    if isinstance(n[1], list):
                        newindent = indent + "  "
                        fmt = "%s\n%s %s%s %s" % (fmt, indent, n[0], indent, out_t(n[1], newindent))
                        continue
                    fmt = "%s\n%s %s - %s" % (fmt, indent, n[0], n[1])
                return fmt
            print out_t(t_out)

        return t_out

    def parse_t(self, lojban):

        fihe_out = run_jbofihe("-t", lojban)

        # it's easier to determine the indentation
        # level if we parse the output backwards
        fihe_tree = fihe_out.split("\n")[::-1]
        fihe_tree.pop(0)

        def dive(tree):

            level = tree[0].find("+")

            if level == -1:
                chunks = tree.pop(0)
                return [(chunks, dive(tree))]

            result = []
            while tree and tree[0][level] in ("+", "|"):
                line = tree[0]
                if line[level] == "+":
                    line =line[level+2:]
                    if ":" in line:
                        t, d = line.split(":")
                        result.append((t.strip(), d.strip()))
                    typ = line
                    tree.pop(0)
                    continue
                elif line[level] == "|":
                    result.append((typ, dive(tree)))
            return result[::-1] # back from backwards parsing

        return dive(fihe_tree)


    def parse_xb(self, lojban):

        fihe_out = run_jbofihe("-x -b", lojban)
        lines = fihe_out.split("\n")
        lines.pop()
        out = map(lambda _: [], range(5))
        for i in range(len(lines) / 5):
            section = lines[5*i:5*(i+1)]
            for j, line in enumerate(section):
                out[j].append(line)
        return map("".join, out)


if __name__ == "__main__":

    import argparse
    cmdline_parser = argparse.ArgumentParser(description='Process some lojban.')
    cmdline_parser.add_argument('words', metavar='word', type=str, nargs='*', help='Some lojban text.',
            default="coi rodo .i mihe jbovla ke skami fanva kehe")
    cmdline_parser.add_argument('--verbose', '-v', action="count", default=0, help='Verbosity, -vv and -vvv are valid.')
    cmdline_parser.add_argument('--translate', '-t', action="store_true", default=False, help='Translate the parsed valsi.')
    args = cmdline_parser.parse_args()

    jbo_parser = LojbanParser(args)
    parsed = jbo_parser.parse(args.words)

    if args.translate:
        from JBO_Translator import JBOTranslator
        print JBOTranslator(args).translate(parsed)
