# -*- coding: UTF-8 -*-
""" Handy dandy helper funxions. """

##
#  Input sanitizing
##

all_chars = ''.join([chr(i) for i in range(128)])
jbo_allowed = "ABCDEFGHIJKLMNOPRSTUVXYZabcdefghijklmnoprstuvxyz'. "
kill_chars = set(all_chars).difference(list(jbo_allowed))

def sanitize_input(inp):

    """ Turn an input into a sane string. """

    global kill_chars

    if type(inp) is str:
        string = inp
    elif type(inp) in (list,tuple):
        string = " ".join(map(str,inp))

    for c in kill_chars:
        string = string.replace(c, "")

    string = string.replace("'", "\'")
    string = string.replace("h", "\'")
    #string = string.lower()

    return string

##
#  Execution helper (for jbofihe).
##

import sh
import sys

def run_jbofihe(args, lojban):
    """ In order to pipe correctly we have to use two commandline wrappers. """
    try:
        return sh.jbofihe(sh.echo(lojban), *args.split())
    except Exception, e:
        print "Got an error: %s" % type(e)
        print "It reads:"
        print e.message
        print "The Exception vanishes in a puff of lojic."
        sys.exit()
    # IMO fabric has the most understandable syntax:
    #cmd = "echo %s | jbofihe %s" % (lojban, args)
    #return local(cmd, capture=True)
