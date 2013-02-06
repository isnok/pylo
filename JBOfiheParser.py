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

        results = [ "Input: %r" % inp ]

        string = self.sanitize_input(inp)

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


