# Generated from Arit1.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t)")
        buf.write("\n\t\r\t\16\t*\3\n\3\n\3\n\3\n\7\n\61\n\n\f\n\16\n\64")
        buf.write("\13\n\3\n\3\n\3\13\5\139\n\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\6\f@\n\f\r\f\16\fA\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5\3\2\62;\4\2\f\f\17")
        buf.write("\17\4\2\13\13\"\"\2H\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31")
        buf.write("\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3")
        buf.write("\2\2\2\r#\3\2\2\2\17%\3\2\2\2\21(\3\2\2\2\23,\3\2\2\2")
        buf.write("\258\3\2\2\2\27?\3\2\2\2\31\32\7*\2\2\32\4\3\2\2\2\33")
        buf.write("\34\7+\2\2\34\6\3\2\2\2\35\36\7=\2\2\36\b\3\2\2\2\37 ")
        buf.write("\7-\2\2 \n\3\2\2\2!\"\7/\2\2\"\f\3\2\2\2#$\7,\2\2$\16")
        buf.write("\3\2\2\2%&\7\61\2\2&\20\3\2\2\2\')\t\2\2\2(\'\3\2\2\2")
        buf.write(")*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\22\3\2\2\2,-\7\61\2\2")
        buf.write("-.\7\61\2\2.\62\3\2\2\2/\61\n\3\2\2\60/\3\2\2\2\61\64")
        buf.write("\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64")
        buf.write("\62\3\2\2\2\65\66\b\n\2\2\66\24\3\2\2\2\679\7\17\2\28")
        buf.write("\67\3\2\2\289\3\2\2\29:\3\2\2\2:;\7\f\2\2;<\3\2\2\2<=")
        buf.write("\b\13\2\2=\26\3\2\2\2>@\t\4\2\2?>\3\2\2\2@A\3\2\2\2A?")
        buf.write("\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\b\f\2\2D\30\3\2\2\2\7\2")
        buf.write("*\628A\3\b\2\2")
        return buf.getvalue()


class Arit1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SCOL = 3
    PLUS = 4
    MINUS = 5
    MULT = 6
    DIV = 7
    INT = 8
    COMMENT = 9
    NEWLINE = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "';'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "SCOL", "PLUS", "MINUS", "MULT", "DIV", "INT", "COMMENT", "NEWLINE", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "SCOL", "PLUS", "MINUS", "MULT", "DIV", 
                  "INT", "COMMENT", "NEWLINE", "WS" ]

    grammarFileName = "Arit1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


