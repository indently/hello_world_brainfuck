"""
Brainfuck.py

This is the main Brainfuck console that combines
all of the interpreters together and surfaces them
all through the command line by calling 'Brainfuck.py'
and setting the appropriate flags.

Please refer to the 'help' strings for each flag for
further information about this module.

If the console has been launched, you will see something
like this prompting you for characters:

>>>

You are free to type any Brainfuck code that you want, and
it will be interpreted and executed automatically. Let's increment
`array[0]` by 40 and then hit ENTER:

>>> ++++++++++++++++++++++++++++++++++++++++
>>>

Want to double check that you in fact added 40 to array[0]? As
`ptr` currently points at zero, you can call `.` to print out
the character stored at array[0], OR you can call the
following special command:

>>> ARRPLZ[0]
-
>>>

`ARRPLZ` can also take arguments in the form of `[start : end]`,
but do note that the endpoint is EXCLUSIVE.

In case you're simply tired of having your brain "fucked with,"
type the following:

>>> GMTFOH

~

FYI: GMTFOH = "Get me the fuck out of here"

Feeling rather adventurous and want to try some EPIC Brainfuck?
Then launch the console with an interpreter other than the "nice"
one! How are things different? Well, first, you need to know what
the eight important characters are so that the modified Brainfuck
will be properly interpreted. You can do so by typing:

>>> HELPPLZ!!!

LONG LIVE BRAINFUCK!

       1 --> >
       q --> ,
       e --> <
       4 --> -
       g --> +
       t --> [
       w --> ]
       . --> .

LONG LIVE THE TROLL!

>>>

For other special commands (i.e. `PTRPLZ`, `ARRPLZ`, and `GMTFOH`),
the interpreter will respond to those commands only 25% of the time.
Yes, that means you will have to type the command about four times
before it will respond. That is the naturing of trolling and further
"fucking with" the mind.

"""
from __future__ import print_function
from argparse import ArgumentParser, \
     RawTextHelpFormatter
from random import choice, random
from re import match
from Trolls import *
from Nice import *

import sys

VERSION = '1.0.2'

if __name__ == '__main__':
    parser = ArgumentParser(description="Brainfuck Interactive Console",
                            formatter_class=RawTextHelpFormatter,
                            add_help=False)
    parser.add_argument("-h", "--help", action="help",
                        help="display documentation\n ")
    parser.add_argument("-i", "--interpreter",
                        type=str, default="nice",
                        help=(
                            "Interpreter specification.\n"
                            "There are six options here:\n\n"
                            "'nice'    - traditional Brainfuck\n"
                            "            interpreter, no shenanigans\n\n"
                            "'reset'   - resets character array to all\n"
                            "            zeros and the array pointer to\n"
                            "            point at that zeroth element of\n"
                            "            that array after each execution\n\n"
                            "'chars'   - changes the eight characters used\n"
                            "            when coding and the semantics behind\n"
                            "            them after each execution\n\n"
                            "'file'    - writes 'LOL' 1000 times to a 'log'\n"
                            "            file after every execution\n\n"
                            "'browser' - opens a tab in your browser playing\n"
                            "            the 'Troll Song' sung by Eduard Khil\n"
                            "            on YouTube after every execution\n\n"
                            "'random'  - choose an interpreter at random\n "))
    parser.add_argument("-l", "--launch", action='store_true',
                        default=False, help=(
                            "Whether or not to launch the\n"
                            "console when Brainfuck code\n"
                            "as been provided. Note that\n"
                            "this argument is not necessary\n"
                            "should no file be provided. The\n"
                            "console will start automatically\n "))
    parser.add_argument("-f", "--file", default=None, type=str,
                        help="Brainfuck file to run (optional)\n ")
    parser.add_argument("-c", "--code", default=None, type=str,
                        help="Brainfuck code to run (optional)\n ")
    parser.add_argument("-v", "--version", action='store_true',
                        default=False, help=("Display Brainfuck "
                                             "interpreter version"))

    args = parser.parse_args()
    interpreter = None
    stdout = False

    if args.version:
        print("Epic Brainfuck {version}".format(version=VERSION))
        sys.exit(0)

    if args.interpreter not in ("nice", "reset", "chars",
                                "file", "browser", "random"):
        print("Invalid interpreter option!")
        sys.exit(1)

    if args.interpreter == "random":
        args.interpreter = choice(["nice", "reset", "chars",
                                   "file", "browser"])

    if args.interpreter == "nice":
        interpreter = NiceInterpreter()

    elif args.interpreter == "reset":
        interpreter = ResetTrollInterpreter()

    elif args.interpreter == "chars":
        interpreter = SetCharsTrollInterpreter()

    elif args.interpreter == "file":
        interpreter = RandomFileTrollInterpreter()

    elif args.interpreter == "browser":
        interpreter = WebbrowserTrollInterpreter()

    else:
        print("Unknown interpreter '{interpreter}'".format(
            interpreter=args.interpreter))
        sys.exit(1)

    # Execute ALL provided code, which means that
    # if both the '-c' and '-f' flags are set, both
    # will be executed
    if args.code is not None:
        interpreter.execute(args.code)

    if args.file is not None:
        if len(args.file) > 3:
            try:
                with open(args.file) as f:
                    code = f.read()
                    interpreter.execute(code)

            except IOError:
                if args.interpreter == 'nice':
                    print("Could not find your file! "
                          "Please double check that the "
                          "path provided is accessible to me.")

                # Troll interpreters provide useless
                # debugging information
                else:
                    print("Your code is broken. It failed.")

                sys.exit(1)

        else:
            if args.interpreter == 'nice':
                print("Invalid Brainfuck File!")

            # Troll interpreters provide useless
            # debugging information
            else:
                print("Your code is broken. It failed.")

            sys.exit(1)

    if (args.code is not None or args.file is not None) and \
       not args.launch:
        sys.exit(0)

    print("Brainfuck Interactive Console")
    print("-----------------------------")

    while True:
        try:
            # Add a newline if there is output
            # to the terminal so that the '>>>'
            # prompt has its own line to itself
            if stdout:
                code = raw_input("\n>>> ")

            else:
                code = raw_input(">>> ")

            # Get me the fuck out of here :)
            if code == 'GMTFOH':
                if args.interpreter == 'nice' or \
                   random() > 0.75:
                    sys.exit(0)

            # Get current 'ptr' value
            elif code == 'PTRPLZ':
                if args.interpreter == 'nice' or \
                   random() > 0.75:
                    print(interpreter.ptr)

            # Get current values of 'array'
            elif match('^ARRPLZ\[\d*:\d*\]$', code) or \
                    match('^ARRPLZ\[\d+]$', code):
                if args.interpreter == 'nice' or \
                   random() > 0.75:
                    indices = code[6:]
                    print(eval("interpreter.array" + indices))

            else:
                stdout = interpreter.execute(code)

        # Protection against seeing the Python internals
        # while running the program, as well as making it
        # more difficult to quit out of it.
        except KeyboardInterrupt:
            stdout = False
