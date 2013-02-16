#!/usr/bin/env python
""" A parser for the official wordlists. """

import os

# as packaged in debian
folder = os.path.sep.join(("", "usr", "share", "lojban"))
gismu_file = os.path.sep.join((folder, "gismu.txt"))

print "Reading gismu file: %s" % gismu_file
gismu_unparsed = [ line.strip() for line in open(gismu_file, "r") ]

from collections import namedtuple
Gismu = namedtuple("Gismu", ["valsi", "rafsi", "gloss", "strange", "trans", "other"]) # to be continued...

valsi_dict = {}

def parse_gismu(line):

    valsi = line[:5].strip()
    line = line[5:]

    rafsi = line[:14].strip().split()
    line = line[14:]

    gloss = line[:21].strip()
    line = line[21:]

    strange = line[:21].strip()
    line = line[21:]

    trans = line[:97].strip()
    line = line[97:]

    other = None # line

    gismu = Gismu(valsi, rafsi, gloss, strange, trans, other)

    valsi_dict[valsi] = gismu
    return gismu


gismu_version = gismu_unparsed.pop(0).strip()
print "Gismu file version: %s" % gismu_version.split()[0]

gismu = map(parse_gismu, gismu_unparsed)


if __name__ == "__main__":

    for idx, g in enumerate(gismu):
        print "%4d: %-5s - %-12s - %s" % (idx, g.valsi, " ".join(g.rafsi), g.gloss)




