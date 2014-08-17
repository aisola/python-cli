#!/usr/bin/env python
import sys

# TODO: Impliment getting info from Environment Variables.
# TODO: Impliment subcommmand applications.

#
# Define the FLAG type constants.
#
F_STRING  = "STRING_FLAG"
F_BOOL    = "BOOLEAN_FLAG"
F_INTEGER = "INTEGER_FLAG"
F_FLOAT   = "FLOAT_FLAG"

#
# CLIParser, a simple, yet effective, argument parser.
#
class CLIParser(object):
    def __init__(self, args):
        self.args   = args
        self.start  = 0   # start position of this item.
        self.pos    = 0   # current position in the input.
        self.rargs  = []
        self.values = {}

    def next(self):
        if self.pos >= len(self.args):
            return None
        arg = self.args[self.pos]
        self.pos += 1
        return arg

    def backup(self):
        self.pos -= 1

    def parse(self):
        # get the first argument
        arg = self.next()
        while True:
            if arg == None:
                break
            elif arg.startswith("--"):
                # it's a long argument
                value = self.next()
                try:
                    if value.startswith("-"):
                        self.values[arg[2:]] = True
                        self.backup()
                    else:
                        self.values[arg[2:]] = value
                except AttributeError:
                    self.values[arg[2:]] = True
            elif arg.startswith("-"):
                # it's a short option
                value = self.next()
                try:
                    if value.startswith("-"):
                        self.values[arg[1:]] = True
                        self.backup()
                    else:
                        self.values[arg[1:]] = value
                except AttributeError:
                    self.values[arg[1:]] = True
            else:
                # it's just an argument
                self.rargs.append(arg)

            # advance the parser
            arg = self.next()

        # the deed is done, let's go
        return self.values, self.rargs

#
# The Flag object defines a flag for the application.
#
class Flag(object):
    def __init__(self, type, name, default=None, usage=""):
        # only 4 kinds of flag
        assert type in [F_STRING, F_BOOL, F_INTEGER, F_FLOAT]
        self.type = type
        # names are defined by a comma separated string
        self.name = name.split(",")
        if default:
            self.default = default
        else:
            # the default `default` is different for each flagtype
            if self.type == F_STRING:
                self.default = ""
            elif self.type == F_BOOL:
                self.default = False
            elif self.type == F_INTEGER:
                self.default = 0
            elif self.type == F_FLOAT:
                self.default == 0.0
        self.usage = usage

#
# Context provides the background under which the application runs.
#
class Context(object):
    def __init__(self, name, flags, args):
        self._name  = name
        self._flags = flags
        self.args  = args

    #
    # Get the vaue of the the given flag.
    #
    def flag(self, name):
        return self._flags.get(name, None)

    #
    # Halt the application and print an error message.
    #
    def error(self, errstr):
        print "%s: FATAL: %s" % (self._name, errstr)
        sys.exit(1)

class CLI(object):
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
            self.flags.append(Flag(F_BOOL, "help", usage="display this help dialog and exit"))
            self.flags.append(Flag(F_BOOL, "version", usage="display version and exit"))
            # Set up parser and parse
            parser = CLIParser(args[1:])
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
