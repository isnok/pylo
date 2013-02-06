#!/usr/bin/env python
""" pylo - a german word play """


def detect_valsi(words):

    """ Detect the valsi of a given input sequence. """

    sounds = " ".join(words)

    return sounds.split(" ")


def detect_wordtypes(words):

    """ Detecets the types of words in the list of valsi. """


    def detect_wordtype(word):
        ln = len(word)
        len_detect = {
                5: "gismu",
                2: "cmavo",
                4: "cmavo",
            }.get(ln)
        if len_detect is None:
            if not ln % 3:
                len_detect = "rafsi"
        return len_detect


    return map(detect_wordtype, words)


def interpret(valsi, types):

    """ Returns a meaning for the given preparsed lojban (hopefully) sentence. """

    return zip(valsi, types)

def nicely(meaning):

    """ Format the interpreted meaning for console output. """

    l1, l2 = [], []
    for (valsi, wordtype) in meaning:
        ln = max(len(valsi), len(wordtype))
        fmt = "%-" + str(ln) + "s"
        l1.append(fmt%valsi)
        l2.append(fmt%wordtype)

    out1, out2 = (" - ".join(l1), " - ".join(l2))
    return "\n".join((out1, out2))



def understand_jbo(words):

    valsi = detect_valsi(words)
    types = detect_wordtypes(valsi)
    meaning = interpret(valsi, types)
    return meaning


if __name__ == "__main__":

    import argparse

    cmdline_parser = argparse.ArgumentParser(description='Process some lojban.')
    cmdline_parser.add_argument('words', metavar='words', type=str, nargs='*', help='some lojban word',
            default="coi rodo .i mi'e jbovlaste ke skami fanva ke'e")

    args = cmdline_parser.parse_args()

    meaning = understand_jbo(args.words)

    print nicely(meaning)

