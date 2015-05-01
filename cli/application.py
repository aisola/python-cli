#!/usr/bin/env python
import sys

from .context import Context
from .flags import Flag, BOOL
from .parser import Parser


class CLI(object):
    "An command line interfaced application."

    def __init__(self, name):
        self.name     = name
        self.version  = "0.0.0"
        self.usage    = ""
        self.flags    = []
        self.action   = None
        self.commands = None


    def _do_help(self):
        print "NAME:"
        print "\t%s - %s" % (self.name, self.usage)
        print "USAGE:"
        print "\t%s [options] [arguments...]" % self.name
        print "VERSION:"
        print "\t%s" % self.version
        print "OPTIONS:"
        for flag in self.flags:
            namestr = flag.name[0]
            for name in flag.name[1:]:
                namestr = namestr + ", %s" % name
            print "\t%s\t\t%s" % (namestr, flag.usage)


    def run(self, args):
        if self.commands == None:
            # add the python-cli flags...
            self.flags.append(Flag(BOOL, "help", usage="display this help dialog and exit"))
            self.flags.append(Flag(BOOL, "version", usage="display version and exit"))
            # Set up parser and parse
            parser = Parser(args[1:])
            flags, args = parser.parse()

            # FIXME: This mess... There might be a better way to do this?
            for flag in self.flags:
                foundname = False
                thenamefound = ""

                # make sure we only have the flag called once
                for name in flag.name:
                    if name in flags.keys():
                        if foundname == False:
                            thenamefound = name
                            foundname = True
                        else:
                            print "%s: FATAL: only use one of %s" % (self.name, flag.name)
                            sys.exit(1)

                # if we found the name, put the others in there so that
                # the user can lookup by any name.
                if foundname:
                    for name in flag.name:
                        flags[name] = flags[thenamefound]

                # otherwise put all in with the default value.
                else:
                    for name in flag.name:
                        flags[name] = flag.default

            # setup the application context and run
            ctx = Context(self.name, flags, args)

            # do automatic version
            if ctx.flag("version"):
                print self.version
                sys.exit(0)

            # do automatic help
            if ctx.flag("help"):
                self._do_help()
                sys.exit(0)

            # finally... do the application
            self.action(ctx)
        else:
            print "cli: FATAL: subcommands not yet implimented"
            sys.exit(1)



