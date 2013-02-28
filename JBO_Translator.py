#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Wordlists import load_files
from Wordlists import valsi_dict
from Wordlists import rafsi_dict

def detect_rafsi(word):
    next_len = False
    if word[:3] in rafsi_dict:
        next_len = 3
    elif word[:4] in rafsi_dict:
        next_len = 4
    return next_len


def translate_valsi(word):
    if word in valsi_dict:
        print "%s : %s" % (word, valsi_dict[word])
    else:
        print "unrecognized: %s" % word

class JBOTranslator:

    def __init__(self, args):
        load_files(args)
        self.verbose = args.verbose

    def translate(self, tree, indent="", do_indent=False):

        def ignore(block):
            ignoreblocks = ("FREE_VOCATIVE", "TEXT", "CHUNKS", "SUMTI", "SELBRI", "TERMS", "CMENE_SEQ", "TANRU", "LINK", "BRIDI_TAIL")
            for ign in ignoreblocks:
                if ign in block:
                    return True
            return False

        def pop_rafsi(valsi, rafsi_len):
            rafsi, rest = rafsi_dict[valsi[:rafsi_len]], valsi[rafsi_len:]
            if not rest:
                return (rafsi,)
            if rest[0] in "y'":
                rest = rest[1:]
            if not rest:
                return (rafsi,)
            next_len = detect_rafsi(rest)
            if next_len:
                try:
                    return (rafsi,) + pop_rafsi(rest, next_len)
                except:
                    print "error parsing: %r" % rest
            return (rafsi,)

        fmt = ""
        for block, words in tree:
            if not isinstance(words, list):
                if " " in words:
                    words = words.split().pop(0)
                if words == "i": # gr. is it a bug?
                    words = ".i"
                if block in ("CMENE", "ZOI"):
                    do_indent = True
                    fmt = "%s\n%s %s (%s) : %s" % (fmt, indent, words, block.lower(), words)
                elif words in valsi_dict:
                    do_indent = True
                    fmt = "%s\n%s %-5s (%s) : %s" % (fmt, indent, words, block.lower(), valsi_dict[words].trans)
                elif detect_rafsi(words):
                    do_indent = True
                    trans = "-".join([r.trans for r in pop_rafsi(words, detect_rafsi(words))])
                    fmt = "%s\n%s %s (%s) : %s" % (fmt, indent, words, block.lower(), trans)
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

if __name__ == "__main__":
    import sys
    for word in sys.argv[1:]:
        translate_valsi(word)
