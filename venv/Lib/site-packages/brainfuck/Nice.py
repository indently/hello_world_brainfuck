"""
Nice.py

Defines traditional Brainfuck interpreters, that is,
Brainfuck interpreters without any shenanigans. This
module is useful for people who are new to Brainfuck
and need time to get used to the original syntax before
undertaking more daunting interpreters like those located
in 'Trolls.py'.

"""
from __future__ import print_function
from Base import Interpreter


__all__ = ['NiceInterpreter']


class NiceInterpreter(Interpreter):
    """
    Traditional Brainfuck interpreter that sticks with the
    original Brainfuck specifications by defining the aliases
    of the eight original Brainfuck characters as themselves.
    It also provides useful error messages for the vast majority
    of cases, which are due to mismatched brackets.

    See Also
    --------
    Interpreter (from Base.py)

    """
    def handleError(self, side='left'):
        """
        Overrides 'handleError' in the base class by providing
        helpful error messages for mismatched brackets depending
        on which side it occurs.

        See Also
        --------
        Interpreter.handleError

        """
        if side == 'left':
            print("Couldn't find matching right bracket")

        elif side == 'right':
            print("Couldn't find matching left bracket")

        else:
            print("An unknown error occurred.")

    def setChars(self):
        """
        Overrides 'setChars' in the base class by setting
        the alias of each of the eight original Brainfuck
        characters as itself.

        See Also
        --------
        Interpreter.setChars

        """
        self.gt = '>'
        self.lt = '<'
        self.plus = '+'
        self.minus = '-'
        self.period = '.'
        self.comma = ','
        self.lbracket = '['
        self.rbracket = ']'
