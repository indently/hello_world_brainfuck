"""
Trolls.py

Defines Brainfuck interpreters intended to further
frustrate users beyond the original frustration of
nearly unreadable code as a result of Brainfuck's
design and construction.

With the bulk of the infrastructure for further
frustration or "trolling" if you will, performed
with the base class 'TrollInterpreter', all that
derived classes have to do is implement the actual
trolling itself.

This module is designed for people who have add
experience coding in Brainfuck and would like to
get their feet wet with EPIC Brainfuck. Good luck
coding in this environment!

"""
from __future__ import print_function
from time import localtime, strftime
from webbrowser import open_new_tab
from Base import TrollInterpreter


__all__ = ['ResetTrollInterpreter', 'SetCharsTrollInterpreter',
           'RandomFileTrollInterpreter', 'WebbrowserTrollInterpreter']


class ResetTrollInterpreter(TrollInterpreter):
    """
    Troll interpreter that resets ``ptr`` and
    ``array`` after every interpretation or execution.

    See Also
    --------
    TrollInterpreter (from Base.py)

    """
    def troll(self):
        """
        Overrides 'troll' in the base class by calling
        'reset'. In traditional Brainfuck, this would never
        be called continuously unless done so explicitly
        by the user or coder.

        See Also
        --------
        TrollInterpreter.troll

        """
        self.reset()


class SetCharsTrollInterpreter(TrollInterpreter):
    """
    Troll interpreter that redefines the eight main
    Brainfuck characters and the semantics behind each
    of them after every interpretation or execution.

    See Also
    --------
    TrollInterpreter (from Base.py)

    """
    def troll(self):
        """
        Overrides 'troll' in the base class by calling
        'setChars'. In traditional Brainfuck, the eight
        characters used in coding are always constant.

        See Also
        --------
        TrollInterpreter.troll

        """
        self.setChars()


class RandomFileTrollInterpreter(TrollInterpreter):
    """
    Troll interpreter that writes to a 'log' file
    useless information after every interpretation
    or execution. Note that it always writes to a
    new 'log' file every time.

    See Also
    --------
    TrollInterpreter (from Base.py)

    """
    def troll(self):
        """
        Overrides 'troll' in the base class by creating
        a new 'log' file and writing useless information
        to it. In this case, it is 100 LOL's.

        See Also
        --------
        TrollInterpreter.troll

        """
        with open('log_{when}.txt'.format(
            when=strftime("%a_%d_%b_%Y_%H_%M_%S", localtime())),
                  'w') as f:
            f.write('LOL\n' * 1000)


class WebbrowserTrollInterpreter(TrollInterpreter):
    """
    Troll interpreter that opens a new tab in one's
    Web browser to a specified link after every
    interpretation or execution.

    See Also
    --------
    TrollInterpreter (from Base.py)

    """
    def troll(self):
        """
        Overrides 'troll' in the base class by opening
        a new tab in one's Web browser to the 'Troll Song'
        sung by Eduard Khil.

        See Also
        --------
        TrollInterpreter.troll

        """
        troll_song = "https://www.youtube.com/watch?v=o1eHKf-dMwo"
        open_new_tab(troll_song)
