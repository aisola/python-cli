#!/usr/bin/env python -O
import sys


class Context(object):
    "Context provides the background under which the application runs."

    def __init__(self, name, flags, args):
        self._name  = name
        self._flags = flags
        self.args  = args


    def flag(self, name):
        return self._flags.get(name, None)


    def error(self, errstr):
        print "%s: FATAL: %s" % (self._name, errstr)
        sys.exit(1)
