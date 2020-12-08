"""
Brainfuck
=========

Provides
    1. Five Brainfuck interpreters, one traditional and four troll
       Refer to documentation in either 'Nice.py' or 'Trolls.py' for
       more information on either.

    2. Brainfuck executable for running Brainfuck code and for coding
       Brainfuck in a more interactive environment.

Documentation
-------------
There are two forms of documentation available. Each Python module has
its own docstring for reference. You can also read the documentation
online at `https://github.com/gfyoung/brainfuck`.

Available modules
-----------------
Base.py
    Base Brainfuck interpreters. They
    serve as the foundation of all
    subsequently defined Brainfuck
    interpreters.

Nice.py
    Traditional Brainfuck interpreters.
    They interpret Brainfuck code as it
    was originally defined.

Trolls.py
    Troll Brainfuck interpreters. While
    they can interpret Brainfuck code as
    it was originally defined, more often
    than not, they will use other characters
    in place of the eight original used. Use
    these interpreters with caution if you're
    not that experienced of a Brainfuck coder!
    Otherwise, enjoy!

Brainfuck.py
    Brainfuck launch console. It can serve a
    variety of purposes, ranging from running
    actual Brainfuck code to serving an interactive
    coding environment for Brainfuck in all of its
    glorious forms, troll and traditional

"""

import os
import sys

if __name__ == 'brainfuck':
    cwd = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, cwd)

    import Base
    import Nice
    import Trolls

    from Base import *
    from Nice import *
    from Trolls import *
    from Brainfuck import VERSION as version

    __all__ = ['version']
    __all__.extend(Base.__all__)
    __all__.extend(Nice.__all__)
    __all__.extend(Trolls.__all__)
