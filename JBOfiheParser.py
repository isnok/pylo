#!/usr/bin/env python

""" A wrapper for the jbofihe parser. """

from commandwrapper import WrapCommand

class LojbanParser:

    """ A wrapper for jbofihe. """

    all_chars = ''.join([chr(i) for i in range(128)])
    jbo_allowed = "ABCDEFGHIJKLMNOPRSTUVXYZabcdefghijklmnoprstuvxyz'. "
    inp_strip = ''.join(set(all_chars).difference(list(jbo_allowed)))

    bin_parser = "jbofihe"
    parser_args = ('-bt -dd', '-ie', '-sev' '-t', '-x -b')

    def sanitize_input(self, inp):

        """ Turn an input into a sane string. """

        if type(inp) is str:
            string = inp
        elif type(inp) is list:
            string = " ".join(inp)

        string = string.strip(self.inp_strip)
        string = string.replace("'", "\\'")
        string = string.replace("h", "\\'")
        #string = string.lower()

        return string


    def parse(self, inp):

        """ Parse the input given. """

        print "Input: %r" % inp
        string = self.sanitize_input(inp)
        print 'Parsing: "%s"' % string.replace('\\','')
        echo_string = WrapCommand("echo %s" % (string,))

        def _exec(args):
            cmdstr = "%s %s" % (self.bin_parser, args)
            cmd = WrapCommand(cmdstr)
            return (args, cmd(echo_string))

        return map(_exec, self.parser_args)


    def format_nicely(self, results):
        nice = ""
        for args, result in results:
            if args == "-x -b":
                lines = result.split("\n")
                lines.pop()
                out = [ [] for _ in range(5) ]
                for i in range(len(lines) / 5):
                    section = lines[5*i:5*(i+1)]
                    for j, line in enumerate(section):
                        out[j].append(line)
                out = map("".join, out)
                nice += "\n---\n%s" % "\n".join(out)

            nice += "\n---\n%s" % result

        return nice


if __name__ == "__main__":

    jbo_parser = LojbanParser()

    import argparse

    cmdline_parser = argparse.ArgumentParser(description='Process some lojban.')
    cmdline_parser.add_argument('words', metavar='word', type=str, nargs='*', help='some lojban word',
            default="coi rodo .i mi'e jbovlaste ke skami fanva ke'e")

    args = cmdline_parser.parse_args()

    results = jbo_parser.parse(args.words)
    print jbo_parser.format_nicely(results)


