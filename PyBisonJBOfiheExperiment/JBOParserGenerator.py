#!/usr/bin/env python

lexscript = "cm_scan.l"
bisonfile = "rpc2x.y"

outfile = "test.py"

tokens = []
bison_code = []

comment = False
for line in open(bisonfile, 'r').readlines():
    if not line.strip():
        continue
    if line.strip().startswith("%token"):
        tokens.append(line.split().pop())
        continue
    if not comment and line.strip().startswith("/*"):
        comment = True
    if not comment:
        bison_code.append(line)
    if comment and line.strip().endswith("*/"):
        comment = False

print "Found %d tokens and %d lines of bison code." % (len(tokens), len(bison_code))

convert = []
unparsed = []

understand = None
for line in bison_code:
    if understand:
        convert.append(line)
    else:
        unparsed.append(line)
    if line.strip() == "%%":
        understand = True

print "Could parse %d and ignored %d lines of bison code." % (len(convert), len(unparsed))


snips = [
'''#!/usr/bin/env python

import bison

class Parser(bison.BisonParser):

    tokens = %s
    precedences=[]

    lexscript = "\\n".join(open("%s", "r").readlines())

    start = "input"

''' % (str(tokens), lexscript),
'''
    def on_%s(self, target, option, names, values):
        """%s"""
        print "on_%s: got %%s %%s %%s %%s" %% (target, option, names, values)
        return
''',
'''
p = Parser()
'''
]


print "Writing to %s." % outfile
open(outfile, "w").write(snips[0])

rule = False
for line in convert:
    if ":" in line:
        if rule:
            print "Error while parsing."
        rule = True
        name = line.split()[0]
        code = line
    if line.strip() == ";":
        if not rule:
            print "Another error while parsing."
        rule = False
        open(outfile, "a").write(snips[1] % (name, code, name))
    if rule:
        code += line



open(outfile, "a").write(snips[2])

print "Done."# snips[2]


'''JBOParser=JBOParser.py

# rapidly create a running, aeh, version :-)
touch $JBOParser
chmod +x $JBOParser

cat > $JBOParser <<ENDOFHACK

p = Parser()
ENDOFHACK
'''
