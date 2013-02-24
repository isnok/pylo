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

    string = string.replace("'", "\\'")
    string = string.replace("h", "\\'")
    #string = string.lower()

    return string

##
#  Execution helper (for jbofihe). no stdout :-(
##
from commandwrapper import WrapCommand

def run_jbofihe(args, lojban):
    """ In order to pipe correctly we have to use two commandline wrappers. """
    echo = WrapCommand("echo %s" % lojban)
    cmd = WrapCommand("jbofihe %s" % args)
    return cmd(echo)
