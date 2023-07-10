#!/usr/bin/python

from textblob import Word
import sys
from functions import *

if len(sys.argv) > 2:
    words = [] 
    for i in sys.argv[2:]:
        words.append(i)
    if sys.argv[1].lower() == "m" or sys.argv[1].lower() == "meaning":
        get_definitions(words)
    elif sys.argv[1].lower() == "s" or sys.argv[1].lower() == "singular":
        get_singular(words)
    elif sys.argv[1].lower() == "p" or sys.argv[1].lower() == "plural":
        get_plural(words)
    elif sys.argv[1].lower() == "c" or sys.argv[1].lower() == "correct":
        get_spell(words)
    elif sys.argv[1].lower() == "sp" or sys.argv[1].lower() == "spellcheck":
        get_spellcheck(words)
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "h" or sys.argv[1] == "help":
        get_help()
