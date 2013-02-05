#!/usr/bin/env python

""" A wrapper for the jbofihe parser. """

from commandwrapper import WrapCommand

class LojbanParser:

    """ A wrapper for jbofihe. """

    bin_parser = "jbofihe"
    parser_args = ('-bt -dd', '-ie', '-sev' '-t', '-x -b')

    def encode(self, string):
        return string.replace("'", "\\'").replace("h", "\\'").lower()

    def parse(self, inp):

        """ Parse the string given. """

        results = [ "Input: %r" % inp ]

        if type(inp) is str:
            string = inp
        elif type(inp) is list:
            string = " ".join(inp)

        string = self.encode(string)
        results.append('Parsing: "%s"' % (string.replace('\\',''),))

        echo_string = WrapCommand("echo %s" % (string,))

        def _exec(args):
            cmdstr = "%s %s" % (self.bin_parser, args)
            cmd = WrapCommand(cmdstr)
            return cmd(echo_string)

        results.extend(map(_exec, self.parser_args))
        return results

    def format_nicely(self, results):
        return "\n---\n".join(results)


if __name__ == "__main__":

    jbo_parser = LojbanParser()

    import argparse

    parser = argparse.ArgumentParser(description='Process some lojban.')
    parser.add_argument('words', metavar='words', type=str, nargs='*', help='some lojban word',
            default="coi rodo .i mi'e jbovlaste ke skami fanva ke'e")
    parser.add_argument('-j', '--jbo', dest='source_lang', action='store_const',
                        const='jbo', default='jbo', help='the source language')

    args = parser.parse_args()

    if args.source_lang == 'jbo':
        results = jbo_parser.parse(args.words)
        print jbo_parser.format_nicely(results)


