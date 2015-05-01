#!/usr/bin/env python
import sys
sys.path.append('../')
import cli

# the action of the program
def main(context):
    if context.flag("lang") == "english":
        print "Hello, friend!"
    elif context.flag("lang") == "spanish":
        print "Hola, amigo!"
    elif context.flag("lang") == "french":
        print "Salut, mon ami!"
    else:
        context.error("unknown language '%s'" % context.flag("lang"))

if __name__ == "__main__":
    APP = cli.CLI("greet")
    APP.version = "0.2"
    APP.usage   = "fight the loneliness!"
    APP.flags   = [
        cli.Flag(cli.STRING, "lang,l", "english", "set the language for the greeting"),
    ]
    APP.action  = main
    APP.run(sys.argv)
