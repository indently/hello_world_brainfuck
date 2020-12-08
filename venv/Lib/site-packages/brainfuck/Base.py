"""
Base.py

Defines all fundamental Brainfuck interpreters that should
then be sub-classed in subsequent modules.

"""
from __future__ import print_function
from sys import stdin, stdout
from random import choice


__all__ = ['Interpreter', 'TrollInterpreter']


class Interpreter(object):
    """
    Base interpreter upon which all other interpreters are derived.
    This base class does much of the heavy lifting, defining all of
    the Brainfuck interpretation and utility functions (e.g. reading
    a single character from STDIN).

    For classes that derive from ``Interpreter``, what is left to override
    are some of the details surrounding the overall functioning of the
    interpreter itself, such as which eight characters to interpret as
    actual Brainfuck code and the semantics behind each of them.

    Attributes
    ----------
    array : list
        A list of 30,000 integers between 0 and 2**7 - 1 which comprise
        something analogous to a character array in C.

    ptr : int
        A pointer to the current index in 'array'.

    gt : str
        An alias for ">" in Brainfuck.

    lt : str
        An alias for "<" in Brainfuck.

    plus : str
        An alias for "+" in Brainfuck.

    minus : str
        An alias for "-" in Brainfuck.

    period : str
        An alias for "." in Brainfuck.

    comma : str
        An alias for "," in Brainfuck.

    lbracket : str
        An alias for "[" in Brainfuck.

    rbracket : str
        An alias for "]" in Brainfuck.

    """
    def __init__(self):
        """
        Initializes an ``Interpreter`` instance. DO NOT OVERRIDE.

        """
        self.reset()
        self.setChars()

    def execute(self, code):
        """
        A wrapper around the ``interpret`` method that allows an
        interpreter to perform other actions before or after actually
        interpreting and executing the passed in Brainfuck code.

        The base method only calls ``interpret``, which is perfectly valid.
        However, if the interpreter intends to do anything else beforehand
        or afterwords, then override this method.

        Parameters
        ----------
        code : str
            The piece of Brainfuck code to be interpreted.

        Returns
        -------
        A boolean indicating whether or not characters were sent to STDOUT

        See Also
        --------
        interpret

        """
        return self.interpret(code)

    def getChar(self):
        """
        Reads a single character from STDIN and stores it in ``array``
        at the current index ``ptr``. DO NOT OVERRIDE.

        """
        self.array[self.ptr] = ord(stdin.read(1))

    def handleError(self, side='left'):
        """
        Handles errors, primarily those with bracket / parentheses matching,
        by informing the user that an error has occurred. How that information
        is performed is completely up to the derived class. DO OVERRIDE.

        Parameters
        ----------
        side : str
            Indicates which side bracket was unable to find a matching bracket
            in a piece of Brainfuck code.

        """
        raise NotImplementedError

    def interpret(self, code):
        """
        Interprets and executes a piece of Brainfuck code. DO NOT OVERRIDE.

        Parameters
        ----------
        code : str
            The piece of Brainfuck code to be interpreted.

        Returns
        -------
        A boolean indicating whether or not characters were sent to STDOUT.
        This boolean is used for formatting purposes when the user is typing
        in Brainfuck directly to the console, and a new string prompt has to
        be displayed to prompt more Brainfuck code.

        """
        stdout = False
        jumps = {}
        index = 0

        while index < len(code):
            char = code[index]

            if char == self.gt:
                self.ptr = (self.ptr + 1) % len(self.array)
                index += 1

            elif char == self.lt:
                self.ptr = (self.ptr - 1) % len(self.array)
                index += 1

            elif char == self.plus:
                self.array[self.ptr] = (self.array[self.ptr] + 1) % 256
                index += 1

            elif char == self.minus:
                self.array[self.ptr] = (self.array[self.ptr] - 1) % 256
                index += 1

            elif char == self.period:
                self.putChar()
                stdout = True
                index += 1

            elif char == self.comma:
                self.getChar()
                index += 1

            elif char == self.lbracket:
                paren = 1

                if self.array[self.ptr] == 0:
                    if index in jumps:
                        index = jumps[index]

                    else:
                        oldindex = index
                        while paren != 0:
                            index += 1

                            if index == len(code) and paren != 0:
                                self.handleError(side='left')
                                return stdout

                            char = code[index]

                            if char == self.lbracket:
                                paren += 1

                            elif char == self.rbracket:
                                paren -= 1

                        jumps[oldindex] = index
                        jumps[index] = oldindex

                index += 1

            elif char == self.rbracket:
                paren = -1

                if self.array[self.ptr] != 0:
                    if index in jumps:
                        index = jumps[index]

                    else:
                        oldindex = index
                        while paren != 0:
                            index -= 1

                            if index < 0 and paren != 0:
                                self.handleError(side='right')
                                return stdout

                            char = code[index]

                            if char == self.lbracket:
                                paren += 1

                            elif char == self.rbracket:
                                paren -= 1

                        jumps[oldindex] = index
                        jumps[index] = oldindex

                index += 1

            else:
                index += 1

        return stdout

    def putChar(self):
        """
        Sends the character stored at current index ``ptr``
        of ``array`` to STDOUT. DO NOT OVERRIDE.

        """
        char = self.array[self.ptr]
        print(chr(char), end='')
        stdout.flush()

    def reset(self):
        """
        Sets ``ptr`` and ``array`` to their initial positions
        for interpreting Brainfuck code. DO NOT OVERRIDE.

        """
        self.ptr = 0
        self.array = [0] * 30000

    def setChars(self):
        """
        Sets the eight characters that will have significant
        meaning when interpreting Brainfuck code. DO OVERRIDE.

        The code below is not meant to be executed but serves
        rather to indicate which eight characters need to be
        "defined" or aliased in an interpreter sub-class.

        """
        self.gt = None
        self.lt = None
        self.plus = None
        self.minus = None
        self.period = None
        self.comma = None
        self.lbracket = None
        self.rbracket = None


gt_signs = ['>', 'a', 'b', 'c', '1']
lt_signs = ['<', 'd', 'e', 'f', '2']
plus_signs = ['+', 'g', 'h', 'i', '3']
minus_signs = ['-', 'j', 'k', 'l', '4']
period_signs = ['.', 'm', 'n', 'o', '5']
comma_signs = [',', 'p', 'q', 'r', '6']
lbracket_signs = ['[', 's', 't', 'u', '7']
rbracket_signs = [']', 'v', 'w', 'x', '8']


class TrollInterpreter(Interpreter):
    """
    Base troll interpreter upon which all other troll interpreters are derived.
    This base class defines further methods upon which to further "frustrate"
    or "fuck with" the user when it comes to interpreting Brainfuck code. Like
    its super class, `TrollInterpreter` does much of the work, such as defining
    the `execute` functionality.

    For classes that derive from ``TrollInterpreter``, what is left to override
    are still some of the details surrounding the overall functioning of the
    interpreter itself, such as how exactly to ``troll`` the user after he or
    she submits a piece Brainfuck code.

    Attributes
    ----------
    aliases : dict
        A mapping between the eight traditional Brainfuck characters and their
        aliases created during the instantiation of ``TrollInterpreter``.

    """
    def handleError(self, side='left'):
        """
        Overrides `handleError` in the base class. DO NOT OVERRIDE.

        See Also
        --------
        Interpreter.handleError

        """
        print("Your code is broken. It failed.")

    def execute(self, code):
        """
        Overrides `execute` in the base class. DO NOT OVERRIDE. This
        implementation wraps the desired `interpret` functionality
        with a `troll` method that should also be overrode in
        derived classes.

        Parameters
        ----------
        code : str
            The piece of Brainfuck code to be interpreted.

        Returns
        -------
        A boolean indicating whether or not characters were sent to STDOUT

        See Also
        --------
        Interpreter.execute

        """
        if code == "HELPPLZ!!!":
            self.printDirective()

        else:
            stdout = self.interpret(code)
            self.troll()

            return stdout

    def printDirective(self):
        """
        Prints out the mapping of aliases to the traditional
        eight Brainfuck characters. DO NOT OVERRIDE.

        """
        print("\nLONG LIVE BRAINFUCK!\n")

        for alias, char in self.aliases.items():
            print("       {alias} --> {char}".format(
                alias=alias, char=char))

        print("\nLONG LIVE THE TROLL!\n")

    def setChars(self):
        """
        Overrides 'setChars' in the base class. DO NOT OVERRIDE.

        Randomly draws from a pre-determined list of aliases for
        each keyword and assigns that alias to the class instance.

        See Also
        --------
        Interpreter.setChars

        """
        self.gt = choice(gt_signs)
        self.lt = choice(lt_signs)
        self.plus = choice(plus_signs)
        self.minus = choice(minus_signs)
        self.period = choice(period_signs)
        self.comma = choice(comma_signs)
        self.lbracket = choice(lbracket_signs)
        self.rbracket = choice(rbracket_signs)

        self.aliases = {
            self.gt: '>',
            self.lt: '<',
            self.plus: '+',
            self.minus: '-',
            self.period: '.',
            self.comma: ',',
            self.lbracket: '[',
            self.rbracket: ']',
        }

    def troll(self):
        """
        Main method that distinguishes a ``TrollInterpreter`` object
        from a more generic ``Interpreter`` object. This method is called
        after every interpretation / execution of Brainfuck code.

        How the 'trolling' is done is completely up to the derived class,
        and there are certainly many ways in which to do so easily in Python.

        """
        raise NotImplementedError
