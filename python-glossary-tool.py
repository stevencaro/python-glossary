#!/usr/bin/python3

import sys

from PythonGlossary import *

glossary = PythonGlossary()

try:
    search_term = sys.argv[1]
    glossary.search(search_term)
except IndexError:
    glossary.rand()

