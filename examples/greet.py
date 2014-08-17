#!/usr/bin/env python
import sys
import cli

# the action of the program
def main(context):
    print "Hello, friend!"

if __name__ == "__main__":
    APP = cli.CLI("greet")
    APP.version = "0.1"
    APP.usage   = "fight the loneliness!"
    APP.action  = main
    APP.run(sys.argv)
