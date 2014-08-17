# Python CLI
Python CLI is simple, fast, and fun package for building command line apps in
Python. The goal is to enable developers to write fast and distributable
command line applications in an expressive way.

This library is based on the [cli.go](https://github.com/codegangsta/cli/)
by [Codegangsta](https://github.com/codegangsta).

## Overview
Command line apps are usually so tiny that there is absolutely no reason why
your code should *not* be self-documenting. Things like generating help text
and parsing command flags/options should not hinder productivity when writing a
command line app.

This is where Python CLI comes into play. Python CLI makes command line
programming fun, organized, and expressive!

## Installation
Make sure you have Python installed and working. Python CLI is built and tested
on Python 2.7, however there are plans to add cross compatibility.

To install Python CLI, simply run:
```
$ git clone https://github.com/aisola/python-cli.git
$ cd python-cli
$ python setup.py install
```

## Getting Started
One of the philosophies behind Python CLI is that an API should be playful and
full of discovery. So, a Python CLI app can be as one line, excluding imports...

``` python
import sys
import cli

cli.CLI("[appname]").run(sys.argv)
```

This app will run and show help text, but is not very useful. Let's give an
action to execute and some help documentation:

``` python
import sys
import cli

def main(context):
    print "BOOM, I say!"

if __name__ == "__main__":
  app := cli.NewApp("boom")
  app.usage = "make an explosive entrance"
  app.action = main
  app.run(sys.argv)
```

Running this already gives you a ton of functionality, plus support for things
like ~~subcommands~~ [subcommands coming soon] and flags, which are covered
below.

## Example

Being a programmer can be a lonely job. Thankfully by the power of automation
that is not the case! Let's create a greeter app to fend off our demons of
loneliness!

``` python
#!/usr/bin/env python
''' greet.py '''
import sys
import cli

def main(context):
    print "Hello, friend!"

if __name__ == "__main__":
  app = cli.CLI("greet")
  app.usage = "fight the loneliness!"
  app.action = main
  app.run(sys.argv)

```

Finally run our new command:

```
$ python greet.py
Hello friend!
```

Python CLI also generates some badass help text:
```
$ greet help
NAME:
    greet - fight the loneliness!
USAGE:
    greet [options] [arguments...]
VERSION:
    0.0.0
COMMANDS:
    help        display this help dialog and exit
    version     display version and exit
```

### Arguments
Arguments passed to your app are stored in the application context that is given
to your action

``` python
...
def main(context):
    print "Hello, friend!"
...
```

### Flags
Setting and querying flags is simple.
``` python
...

def main(context):
    if context.flag("lang") == "english":
        print "Hello, friend!"
    elif context.flag("lang") == "spanish":
        print "Hola, amigo!"
    elif context.flag("lang") == "french":
        print "Salut, mon ami!"
    else:
        # error stops the app and displays the message!
        context.error("unknown language '%s'" % context.flag("lang"))

...

app.flags = [
    cli.Flag(cli.F_STRING, "lang,l", default="english", usage="set the language for the greeting"),
]
app.action = main
...
```

#### Alternate Names

You can set alternate (or short) names for flags by providing a comma-delimited
list for the Name. e.g.

``` python
app.flags = [
    cli.Flag(F_STRING, "lang,l", default="english", usage="language for the greeting"),
]
```

<!-- #### Values from the Environment

You can also have the default value set from the environment via EnvVar.  e.g.

``` python TODO: this
app.flags = [
    cli.Flag(F_STRING, "lang,l", default="english",
                usage="language for the greeting",
                env="GREET_LANGUAGE"),
]
```

That flag can then be set with `--lang spanish` or `-l spanish`. Note that
giving two different forms of the same flag in the same command invocation is an
error.
-->

<!-- ### Subcommands TODO: this

Subcommands can be defined for a more git-like command line app.
```go
...
app.Commands = []cli.Command{
  {
    Name:      "add",
    ShortName: "a",
    Usage:     "add a task to the list",
    Action: func(c *cli.Context) {
      println("added task: ", c.Args().First())
    },
  },
  {
    Name:      "complete",
    ShortName: "c",
    Usage:     "complete a task on the list",
    Action: func(c *cli.Context) {
      println("completed task: ", c.Args().First())
    },
  },
  {
    Name:      "template",
    ShortName: "r",
    Usage:     "options for task templates",
    Subcommands: []cli.Command{
      {
        Name:  "add",
        Usage: "add a new template",
        Action: func(c *cli.Context) {
            println("new task template: ", c.Args().First())
        },
      },
      {
        Name:  "remove",
        Usage: "remove an existing template",
        Action: func(c *cli.Context) {
          println("removed task template: ", c.Args().First())
        },
      },
    },
  },
}
...
```
-->

## Contribution Guidelines
Feel free to put up a pull request to fix a bug or maybe add a feature. I will
give it a code review and make sure that it does not break backwards
compatibility. If I or any other collaborators agree that it is in line with
the vision of the project, we will work with you to get the code into a
mergeable state and merge it into the master branch.

## License
Python CLI is licensed under the MIT License.

```
Copyright (C) 2014 Abram C. Isola
All Rights Reserved.

MIT LICENSE

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
