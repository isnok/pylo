#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" A parser for the official wordlists. """

verbose = 0

import os

##
#  the dicts
##

valsi_dict = {}
rafsi_dict = {}


##
#  the txts
##

cmavo = None
gismu = None
rafsi = None


##
#  The 'smart' datatypes (drafted;)
##

from collections import namedtuple
Cmavo = namedtuple("Cmavo", ["valsi", "clas", "gloss", "trans"])
Gismu = namedtuple("Gismu", ["valsi", "rafsi", "gloss", "strange", "trans", "other"]) # to be continued...
Rafsi = namedtuple("Rafsi", ["valsi", "gismu", "gloss", "trans"])

def add_translation(key, data, dct):
    if not key in dct:
        dct[key] = data
    else:
        if verbose > 2:
            print "WARNING: Double translation of %r." % key
            print "New version   (%d): %s" % (len(data.trans), data.trans)
            print "Other version (%d): %s" % (len(dct[key].trans), dct[key].trans)
        dct[key] = data
        #this uses the longer translation
        #dct[key] = max(data, dct[key], key=lambda v: len(v.trans))


##
#  parse functions
##

def parse_cmavo(line):

    valsi = line[:10].strip()
    line = line[10:]

    clas = line[:9].strip().split()
    line = line[9:]

    gloss = line[:42].strip()
    line = line[42:]

    trans = line.strip()

    new_cmavo = Cmavo(valsi, clas, gloss, trans)

    add_translation(valsi, new_cmavo, valsi_dict)
    return new_cmavo

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

    other = line

    new_gismu = Gismu(valsi, rafsi, gloss, strange, trans, other)

    add_translation(valsi, new_gismu, valsi_dict)
    return new_gismu

def parse_rafsi(line):

    valsi = line[:5].strip()
    line = line[5:]

    gism = line[:6].strip().split()
    line = line[6:]

    gloss = trans = line.strip()

    new_rafsi = Rafsi(valsi, gism, gloss, trans)

    add_translation(valsi, new_rafsi, rafsi_dict)
    return new_rafsi


##
#  load files.
#
#  defaults are as packaged in debian (in lojban-common)
##

def load_files(args=None):

    if args:
        verbose = args.verbose

    global valsi_dict, rafsi_dict
    global cmavo, gismu, rafsi

    folder = os.path.sep.join(("", "usr", "share", "lojban"))
    cmavo_file = os.path.sep.join((folder, "cmavo.txt"))
    gismu_file = os.path.sep.join((folder, "gismu.txt"))
    rafsi_file = os.path.sep.join((folder, "rafsi.txt"))

    ##
    #  gismu.txt + cmavo.txt
    #
    #  in that order, cause the cmavo translations
    #  here and there seem to be improved versions
    #  of their gismu counterfeits.
    ##

    if verbose > 1:
        print "Reading gismu file: %s" % gismu_file
    gismu_unparsed = [ line.strip() for line in open(gismu_file, "r") ]

    gismu_version = gismu_unparsed.pop(0).strip()
    if verbose:
        print "Gismu file version: %s" % gismu_version.split()[0]

    gismu = map(parse_gismu, gismu_unparsed)


    if verbose > 1:
        print "Reading cmavo file: %s" % cmavo_file
    cmavo_unparsed = [ line.strip() for line in open(cmavo_file, "r") ]

    cmavo_version = cmavo_unparsed.pop(0).strip()
    if verbose:
        print "Cmavo file version: %s" % cmavo_version.split()[0]

    cmavo = map(parse_cmavo, cmavo_unparsed)

    ##
    #  rafsi.txt
    ##

    if verbose > 1:
        print "Reading rafsi file: %s" % rafsi_file
    rafsi_unparsed = [ line.strip() for line in open(rafsi_file, "r") ]

    rafsi = map(parse_rafsi, rafsi_unparsed)

if __name__ == "__main__":

    verbose = 1
    load_files()

    for idx, g in enumerate(gismu):
        print "%4d: %-5s - %-12s - %s" % (idx, g.valsi, g.gloss, g.trans)
    for idx, c in enumerate(cmavo):
        print "%4d: %-5s - %-12s - %s" % (idx, c.valsi, c.gloss, c.trans)
    for idx, r in enumerate(rafsi):
        print "%4d: %-5s - %-12s - %s" % (idx, r.valsi, r.gloss, r.trans)
