#!/usr/bin/env python

""" A wrapper for the jbofihe parser. """

from commandwrapper import WrapCommand

from Wordlists import valsi_dict

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
    inp_strip = ''.join(set(all_chars).difference(list(jbo_allowed)))

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

        print xb_out[0]


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
