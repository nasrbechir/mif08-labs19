# LAB2, arithmetic expressions interpretor
MIF08, January 2020, Laure Gonnord & Matthieu Moy


# Content

This directory contains an interpretor for simple arithmetical
expressions like 5+3, for instance. The intepretor evaluates the
arithmetical expressions and prints their value on the standard
output.

# Usage

* `make` to generate Arit1Lexer.py and Arit1Parser.py (once)

* `python3 arit1.py <path/and/test/name>` to test a given file, for
 instance: 
 `python3 arit1.py testfiles/test01.txt`  should print `1+2 = 3`

* `make tests` to test on all tests files of the `testfile` directory

# Syntax of our language/restrictions

The syntax is the one textually given in the Lab2 sheet. 
Restriction : we did not implement minus nor unary minus.

# Design choices

* Arit1.g4 contains the lexical, syntactic descriptions as well as
  semantic actions in Python.
* In the main file arit1.py we have chosen to stop our interpret as
  soon as we get a lex or grammar error.

# Known bugs

N/A
