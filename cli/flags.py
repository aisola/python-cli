#!/usr/bin/env python -O


# Define the FLAG type constants.
STRING  = "STRING_FLAG"
BOOL    = "BOOLEAN_FLAG"
INTEGER = "INTEGER_FLAG"
FLOAT   = "FLOAT_FLAG"



class Flag(object):
    "The Flag object defines a flag for the application."

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
                self.default = 0.0
        self.usage = usage
