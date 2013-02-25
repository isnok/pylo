#!/usr/bin/env python
""" A parser for the official wordlists. """

valsi_dict = {}
rafsi_dict = {}

import os

# as packaged in debian (in lojban-common)
folder = os.path.sep.join(("", "usr", "share", "lojban"))

##
#  gismu.txt
##

gismu_file = os.path.sep.join((folder, "gismu.txt"))

print "Reading gismu file: %s" % gismu_file
gismu_unparsed = [ line.strip() for line in open(gismu_file, "r") ]

from collections import namedtuple
Gismu = namedtuple("Gismu", ["valsi", "rafsi", "gloss", "strange", "trans", "other"]) # to be continued...

def parse_gismu(line):

    valsi = line[:5].strip()
    line = line[5:]

    if valsi in valsi_dict:
        print "WARNING: Overwriting double translation of %r." % valsi

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



##
#  cmavo.txt
##

cmavo_file = os.path.sep.join((folder, "cmavo.txt"))

print "Reading cmavo file: %s" % cmavo_file
cmavo_unparsed = [ line.strip() for line in open(cmavo_file, "r") ]

from collections import namedtuple
Cmavo = namedtuple("Cmavo", ["valsi", "clas", "gloss", "trans"])

def parse_cmavo(line):

    valsi = line[:10].strip()
    line = line[10:]

    if valsi in valsi_dict:
        print "WARNING: Overwriting double translation of %r." % valsi

    clas = line[:9].strip().split()
    line = line[9:]

    gloss = line[:42].strip()
    line = line[42:]

    trans = line.strip()

    cmavo = Cmavo(valsi, clas, gloss, trans)

    valsi_dict[valsi] = cmavo
    return cmavo


cmavo_version = cmavo_unparsed.pop(0).strip()
print "Cmavo file version: %s" % cmavo_version.split()[0]

cmavo = map(parse_cmavo, cmavo_unparsed)

##
#  rafsi.txt
##

rafsi_file = os.path.sep.join((folder, "rafsi.txt"))

print "Reading rafsi file: %s" % rafsi_file
rafsi_unparsed = [ line.strip() for line in open(rafsi_file, "r") ]

from collections import namedtuple
Rafsi = namedtuple("Rafsi", ["valsi", "gismu", "gloss", "trans"])

def parse_rafsi(line):

    valsi = line[:5].strip()
    line = line[5:]

    gism = line[:6].strip().split()
    line = line[6:]

    gloss = trans = line.strip()

    rafsi = Rafsi(valsi, gism, gloss, trans)

    rafsi_dict[valsi] = rafsi
    return rafsi

rafsi = map(parse_rafsi, rafsi_unparsed)

if __name__ == "__main__":

    for idx, g in enumerate(rafsi):
        print "%4d: %-5s - %-12s - %s" % (idx, g.valsi, g.gloss, g.trans)
