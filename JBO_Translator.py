from Wordlists import valsi_dict
from Wordlists import rafsi_dict

class JBOTranslator:

    def translate(self, tree, indent="", do_indent=False):

        def ignore(block):
            ignoreblocks = ("FREE_VOCATIVE", "TEXT", "CHUNKS", "SUMTI", "SELBRI", "TERMS", "CMENE_SEQ")
            for ign in ignoreblocks:
                if ign in block:
                    return True
            return False

        def pop_rafsi(valsi, rafsi_len):
            rafsi, rest = rafsi_dict[valsi[:rafsi_len]], valsi[rafsi_len:]
            if not rest:
                return (rafsi,)
            if rest[0] in "y'":
                rest = rest[0:]
            elif rest[:3] in rafsi_dict:
                next_len = 3
            elif rest[:4] in rafsi_dict:
                next_len = 4
            return (rafsi,) + pop_rafsi(rest, next_len)

        fmt = ""
        for block, words in tree:
            if type(words) is str:
                if " " in words:
                    words = words.split().pop(0)
                if words == "i": # gr. is it a bug?
                    words = ".i"
                if block == "CMENE":
                    do_indent = True
                    fmt = "%s\n%s %s - %s : %s" % (fmt, indent, block, words, words)
                elif words in valsi_dict:
                    do_indent = True
                    fmt = "%s\n%s %-5s (%s) : %s" % (fmt, indent, words, block.lower(), valsi_dict[words].trans)
                elif words[:3] in rafsi_dict:
                    do_indent = True
                    trans = "-".join([r.trans for r in pop_rafsi(words, 3)])
                    fmt = "%s\n%s %s (%s) : %s" % (fmt, indent, words, block.lower(), trans)
                elif words[:4] in rafsi_dict:
                    do_indent = True
                    trans = "-".join([r.trans for r in pop_rafsi(words, 4)])
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
