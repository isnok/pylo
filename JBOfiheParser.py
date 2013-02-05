#!/usr/bin/env python

""" A wrapper for the jbofihe parser. """

from commandwrapper import WrapCommand

class LojbanParser:

    bin_parser = "jbofihe"
    parser_args = ('', '-t', '-x -b')

    def parse(self, inp):

        """ Parse the string given. """

        print "Input: %r" % inp

        if type(inp) is str:
            string = inp
        elif type(inp) is list:
            string = " ".join(inp)

        string = string.replace("'", "\\'").replace("h", "\\'").lower()

        echo_string = WrapCommand("echo %s" % (string,))
        cmdstrs = [ "%s %s" % (self.bin_parser, args) for args in self.parser_args ]

        def _exec(cmdstr):
            cmd = WrapCommand(cmdstr)
            return cmd(echo_string)

        results = map(_exec, cmdstrs)
        return results

    def format_nicely(self, results):
        return "\n---\n".join(results)

if __name__ == "__main__":

    jbo_parser = LojbanParser()

    #jbo_parser.parse("coi")

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('words', metavar='words', type=str, nargs='*', help='some lojban word')
    parser.add_argument('-j', '--jbo', dest='source_lang', action='store_const',
                        const='jbo', default='jbo', help='the source language')

    args = parser.parse_args()

    if args.source_lang == 'jbo':
        results = jbo_parser.parse(args.words)
        print jbo_parser.format_nicely(results)


