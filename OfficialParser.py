#!/usr/bin/env python

""" A wrapper for the official parser. """

from commandwrapper import WrapCommand

class LojbanParser:

    bin_parser = "contrib/parser-3.0.00/parser"
    parser_args = '' #'-d"*"'
    parse_cmd = WrapCommand("%s %s" % (bin_parser, parser_args))

    def parse(self, string):

        """ Parse the string given. """

        echo_cmd = WrapCommand("echo %s" % (string,))
        return self.parse_cmd(echo_cmd)


if __name__ == "__main__":

    jbo_parser = LojbanParser()

    import argparse

    cmdline_parser = argparse.ArgumentParser(description='Process some lojban.')
    cmdline_parser.add_argument('words', metavar='word', type=str, nargs='*', help='some lojban word',
            default="coi rodo .i mi'e jbovlaste ke skami fanva ke'e")

    args = cmdline_parser.parse_args()

    print jbo_parser.parse(args.words)
