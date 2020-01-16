#! /usr/bin/env python3
"""
Usage:
    python3 sujetA.py <filename>
"""
# Main file for MIF08 - Labxx - 2019-20

from SujetALexer import SujetALexer
from SujetAParser import SujetAParser
from antlr4 import FileStream, StdinStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
# generic main files to test grammars

import argparse

""" Main file for ANTLR Grammar testing (lab evaluation)
usage : python3 sujetA.py <filetotest>
1- if the file launches any lexical error, it silently catches it and exit with code 1 (and prints "lexical error")
2- if the file launches any syntax error, same with exitcode 2 and "syntax error"
3- if the file is conform to the grammar, it exits with exicode 0 and "ok!"

"""

class CountErrorListener(ErrorListener):
    """Count number of errors.

    Parser provides getNumberOfSyntaxErrors(), but the Lexer
    apparently doesn't provide an easy way to know if an error occured
    after the fact. Do the counting ourserves with a listener.
    """

    def __init__(self):
        super(CountErrorListener, self).__init__()
        self.count = 0

    def tokenRecognitionError(self):
        self.count += 1

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.count += 1


def main(inputname, verbose):
    if inputname:
        lexer = SujetALexer(FileStream(inputname))
    else:
        lexer = SujetALexer(StdinStream())
    if not verbose:
        lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)
    counter = CountErrorListener()
    lexer._listeners.append(counter)
    stream = CommonTokenStream(lexer)
    stream.fill()
    if counter.count > 0:  # wrong token !
        print("lexical error")
        exit(1)
    parser = SujetAParser(stream)
    if not verbose:
        parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
    parser._listeners.append(counter)
    parser.start()
    if counter.count > 0:
        print("syntax error")
        exit(2)
    else:
        print("ok")
        exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Grammar demo')
    parser.add_argument('filename', type=str, nargs='?',
                        help='Source file.')
    parser.add_argument('--verbose', action='store_true',
                        help='Show error messages')
    args = parser.parse_args()
    main(args.filename, args.verbose)
