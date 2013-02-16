#!/usr/bin/env python

""" A wrapper for the jbofihe parser. """

from commandwrapper import WrapCommand

from Wordlists import valsi_dict
from Wordlists import rafsi_dict

def run_jbofihe(args, lojban):
    """ In order to pipe correctly we have to use two commandline wrappers. """
    echo = WrapCommand("echo %s" % lojban)
    cmd = WrapCommand("jbofihe %s" % args)
    return cmd(echo)



class LojbanParser:

    """ A wrapper for jbofihe. """

    verbose = True

    all_chars = ''.join([chr(i) for i in range(128)])
    jbo_allowed = "ABCDEFGHIJKLMNOPRSTUVXYZabcdefghijklmnoprstuvxyz'. "
    inp_strip = set(all_chars).difference(list(jbo_allowed))

    def sanitize_input(self, inp):

        """ Turn an input into a sane string. """

        if type(inp) is str:
            string = inp
        elif type(inp) is list:
            string = " ".join(inp)

        for c in self.inp_strip:
            string = string.replace(c, "")

        string = string.replace("'", "\\'")
        string = string.replace("h", "\\'")
        #string = string.lower()

        return string


    def parse(self, inp):

        """ Parse the input given. """

        if self.verbose:
            print "Input: %r" % inp

        string = self.sanitize_input(inp)

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
                    if type(n[1]) is str:
                        fmt = "%s\n%s %s - %s" % (fmt, indent, n[0], n[1])
                        continue
                    newindent = indent + "  "
                    fmt = "%s\n%s %s%s %s" % (fmt, indent, n[0], indent, out_t(n[1], newindent))
                    #newindent = indent + (" " * (1 + len(n[0])))
                    #fmt = "%s\n%s %s\n%s %s" % (fmt, indent, n[0], indent, out_t(n[1], newindent))
                return fmt
            print out_t([t_out])

        print self.translate([t_out])
        #import MetaTree
        #MetaTree.NodeTree(t_out).pprint()


    def translate(self, tree, indent="", do_indent=False):

        def ignore(block):
            ignoreblocks = ("FREE_VOCATIVE", "TEXT", "CHUNKS", "SUMTI", "SELBRI", "TERMS", "CMENE_SEQ")
            for ign in ignoreblocks:
                if ign in block:
                    return True
            return False

        def pop_rafsi(valsi):
            if not valsi:
                return ()
            if valsi[:3] in rafsi_dict:
                return (rafsi_dict[valsi[:3]],) + pop_rafsi(valsi[3:])
            if valsi[:4] in rafsi_dict:
                return (rafsi_dict[valsi[:4]],) + pop_rafsi(valsi[4:])

        fmt = ""
        for block, words in tree:
            if type(words) is str:
                if " " in words:
                    words = words.split().pop(0)
                if words == "i": # gr. is it a bug?
                    words = ".i"
                if block == "CMENE":
                    do_indent = True
                    fmt = "%s\n%s %s - %s : %s" % (fmt, indent, block, words, words)
                elif words in valsi_dict:
                    do_indent = True
                    fmt = "%s\n%s %s - %s : %s" % (fmt, indent, block, words, valsi_dict[words].trans)
                elif words[:3] in rafsi_dict or words[:4] in rafsi_dict:
                    do_indent = True
                    trans = "-".join([r.trans for r in pop_rafsi(words)])
                    fmt = "%s\n%s %s - %s : %s" % (fmt, indent, block, words, trans)
                else:
                    if not ignore(block):
                        do_indent = True
                        fmt = "%s\n%s %s - %s" % (fmt, indent, block, words)
                continue
            newindent = indent
            if do_indent:
                newindent = indent + "  "
            if not ignore(block):
                do_indent = True
                fmt = "%s\n%s %s%s %s" % (fmt, indent, block, indent, self.translate(words, newindent, do_indent))
            else:
                fmt = "%s%s" % (fmt, self.translate(words, newindent, do_indent))
            #newindent = indent + (" " * (1 + len(n[0])))
            #fmt = "%s\n%s %s\n%s %s" % (fmt, indent, n[0], indent, out_t(n[1], newindent))
        return fmt


    def parse_t(self, lojban):

        fihe_out = run_jbofihe("-t", lojban)

        fihe_tree = fihe_out.split("\n")[::-1]
        fihe_tree.pop(0)

        def dive(tree):

            level = tree[0].find("+")

            if level == -1:
                chunks = tree.pop(0)
                return (chunks, dive(tree))

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
            return result[::-1]

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

    #parser_args = ('-bt -dd', '-ie', '-sev' '-t', '-x -b')
    jbo_parser = LojbanParser()

    import argparse

    cmdline_parser = argparse.ArgumentParser(description='Process some lojban.')
    cmdline_parser.add_argument('words', metavar='word', type=str, nargs='*', help='some lojban word',
            default="coi rodo .i mi'e jbovla ke skami fanva ke'e")

    args = cmdline_parser.parse_args()

    jbo_parser.parse(args.words)
