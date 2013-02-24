#!/usr/bin/env python

import bison

bison.bisonToPython("uncomm.y", "cm_scan.l", "parser.py")
