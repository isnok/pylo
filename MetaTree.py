#!/usr/bin/env python

from collections import Callable


def keyiter(orig):
    if type(orig) in (list, tuple):
        return xrange(len(orig))
    elif type(orig) == dict:
        return orig.iterkeys()
    raise TypeError("Cannot get key iterator for %r" % (orig,))


def setappend(dct, key, value):
    """ used instead of defaultdict for read-only situations """
    if key in dct:
        dct[key].append(value)
    else:
        dct[key] = [value]


class NodeTree(Callable):

    def __init__(self, original=None):
        self.nodes = {}
        self.children = {}
        self.nodetypes = {}
        if original is not None:
            self._original = original
            self.populate(original)

    def populate(self, structure, path=()):
        path = tuple(path)
        self.nodes[path] = structure
        setappend(self.nodetypes, type(structure), path)
        try:
            for k in keyiter(structure):
                setappend(self.children, path, k)
                self.populate(structure[k], path + (k,))
        except TypeError: # it's a leaf
            pass

    def getdata(self, path):
        return self.nodes[tuple(path)]

    def getlist(self, paths, giveNones=False):
        result = []
        for path in paths:
            try:
                result.append(self.nodes[tuple(path)])
            except:
                if giveNones:
                    result.append(None)
        return result

    def validate(self, path):
        return tuple(path) in self.nodes

    def __call__(self, *args):
        return self.getdata(args)

    def __repr__(self):
        return "%s%r" % (self.__class__.__name__, sorted(self.nodes.keys()))

    def __str__(self):
        return "%s%r" % (self.__class__.__name__, sorted(self.getleaves()))

    def gettypednodes(self, typ):
        return self.nodetypes[typ]

    def isleaf(self, path):
        try:
            return not bool(self.children[tuple(path)])
        except KeyError:
            return True

    def getleaves(self, path=()):
        return [ p for p in self.nodes if self.isleaf(p) ]

    def getchildren(self, path):
        try:
            return self.children[tuple(path)]
        except KeyError:
            return []

    def getallchildren(self, path=(), condition=lambda path, data: True):
        children = []
        try:
            if condition(path, self.getdata(path)):
                children.append(path)
        except: # failing conditions should be False
            pass
        for c in self.getchildren(path):
            children.extend([cp for cp in self.getallchildren(path + (c,), condition)])
        return children

    def getWildcardPaths(self, wcpath):
        if "**" in wcpath[:-1]:
            raise KeyError(wcpath)
        tmp = [ () ]
        for key in wcpath:
            if key == "*":
                result = []
                for t in tmp:
                    result.extend([ t + (c,) for c in self.getchildren(t) ])
            else:
                result = [ r + (key,) for r in tmp ]
            tmp = result

        if "**" in wcpath[-1:]:
            result = []
            for t in tmp:
                result.extend([ t[:-1] + cp[len(t)-1:] for cp in self.getallchildren(t[:-1]) ])

        return result

    def subtree(self, path):
        """ returns a new tree (that doesn't know of it's parent) """
        return self.__class__(self.getdata(path))

    def dump(self):
        dump = "%s:\n" % (self.__class__.__name__)
        keys = list(sorted(self.nodes.keys()))
        if keys:
            for path in keys[:-1]:
                dump += " |- %r -> %r\n" % (path, self.getdata(path))
            dump += " `- %r -> %r\n" % (keys[-1], self.getdata(keys[-1]))
        else:
            dump += " `- (empty)"
        return dump

    def pformat(self, path=(), indent="", first=True, last=True):
        if first:
            fmt = self.__class__.__name__ + "\n"
        else:
            fmt = ""
        childkeys = sorted(self.getchildren(path))
        if childkeys:
            printdata = type(self.getdata(path))
        else:
            printdata = self.getdata(path)
        if last:
            fmt = "%s%s `- %r -> %r\n" % (fmt, indent, path[-1:], printdata)
            indent += "    "
        else:
            fmt = "%s%s |- %r -> %r\n" % (fmt, indent, path[-1:], printdata)
            indent += " |  "
        if childkeys:
            fmt = "%s%s |\n" % (fmt, indent)
        else:
            fmt = "%s%s\n" % (fmt, indent)
        children = [path + (c,) for c in childkeys]
        if children:
            for child in children[:-1]:
                fmt += self.pformat(child, indent, last=False, first=False)
            fmt += self.pformat(children[-1], indent, last=True, first=False)
        return fmt

    def pprint(self, path=()):
        print self.pformat(path)
