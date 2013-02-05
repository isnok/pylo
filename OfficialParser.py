#!/usr/bin/env python

""" A wrapper for the official parser. """

from commandwrapper import WrapCommand

class LojbanParser:

    bin_parser = "contrib/parser-3.0.00/parser"
    parser_args = '-d"*"'
    parse_cmd = WrapCommand("%s %s" % (bin_parser, parser_args))

    def parse(self, string):

        """ Parse the string given. """

        echo_cmd = WrapCommand("echo %s" % (string,))
        return self.parse_cmd(echo_cmd)


if __name__ == "__main__":

    jbo_parser = LojbanParser()

    #jbo_parser.parse("coi")

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('word', type=str, nargs='*', help='some lojban word')
    parser.add_argument('-j', '--jbo', dest='source_lang', action='store_const',
                        const='jbo', default='jbo', help='the source language')

    args = parser.parse_args()

    if args.source_lang == 'jbo':
         print jbo_parser.parse(args.word)

