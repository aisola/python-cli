#!/usr/bin/env python -O


class Parser(object):
    "A simple, yet effective argument parser."

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
