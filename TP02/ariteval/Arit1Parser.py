# Generated from Arit1.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4$\n\4\f\4\16\4\'")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\60\n\5\3\5\2\3\6")
        buf.write("\6\2\4\6\b\2\2\2\61\2\13\3\2\2\2\4\21\3\2\2\2\6\25\3\2")
        buf.write("\2\2\b/\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r")
        buf.write("\13\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20")
        buf.write("\3\3\2\2\2\21\22\5\6\4\2\22\23\7\5\2\2\23\24\b\3\1\2\24")
        buf.write("\5\3\2\2\2\25\26\b\4\1\2\26\27\5\b\5\2\27\30\b\4\1\2\30")
        buf.write("%\3\2\2\2\31\32\f\5\2\2\32\33\7\b\2\2\33\34\5\6\4\6\34")
        buf.write("\35\b\4\1\2\35$\3\2\2\2\36\37\f\4\2\2\37 \7\6\2\2 !\5")
        buf.write("\6\4\5!\"\b\4\1\2\"$\3\2\2\2#\31\3\2\2\2#\36\3\2\2\2$")
        buf.write("\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\7\3\2\2\2\'%\3\2\2\2(")
        buf.write(")\7\n\2\2)\60\b\5\1\2*+\7\3\2\2+,\5\6\4\2,-\7\4\2\2-.")
        buf.write("\b\5\1\2.\60\3\2\2\2/(\3\2\2\2/*\3\2\2\2\60\t\3\2\2\2")
        buf.write("\6\r#%/")
        return buf.getvalue()


class Arit1Parser ( Parser ):

    grammarFileName = "Arit1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SCOL", "PLUS", 
                      "MINUS", "MULT", "DIV", "INT", "COMMENT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_atom = 3

    ruleNames =  [ "prog", "statement", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SCOL=3
    PLUS=4
    MINUS=5
    MULT=6
    DIV=7
    INT=8
    COMMENT=9
    NEWLINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Arit1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Arit1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Arit1Parser.StatementContext,i)


        def getRuleIndex(self):
            return Arit1Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Arit1Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==Arit1Parser.T__0 or _la==Arit1Parser.INT):
                    break

            self.state = 13
            self.match(Arit1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(Arit1Parser.ExprContext,0)


        def SCOL(self):
            return self.getToken(Arit1Parser.SCOL, 0)

        def getRuleIndex(self):
            return Arit1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Arit1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            localctx._expr = self.expr(0)
            self.state = 16
            self.match(Arit1Parser.SCOL)
            print((None if localctx._expr is None else self._input.getText((localctx._expr.start,localctx._expr.stop)))+" = "+str(localctx._expr.val))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None
            self.e1 = None # ExprContext
            self.a = None # AtomContext
            self.e2 = None # ExprContext

        def atom(self):
            return self.getTypedRuleContext(Arit1Parser.AtomContext,0)


        def MULT(self):
            return self.getToken(Arit1Parser.MULT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Arit1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Arit1Parser.ExprContext,i)


        def PLUS(self):
            return self.getToken(Arit1Parser.PLUS, 0)

        def getRuleIndex(self):
            return Arit1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Arit1Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            localctx.a = self.atom()
            localctx.val=localctx.a.val
            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = Arit1Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 24
                        self.match(Arit1Parser.MULT)
                        self.state = 25
                        localctx.e2 = self.expr(4)
                        localctx.val=localctx.e1.val*localctx.e2.val
                        pass

                    elif la_ == 2:
                        localctx = Arit1Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 29
                        self.match(Arit1Parser.PLUS)
                        self.state = 30
                        localctx.e2 = self.expr(3)
                        localctx.val=localctx.e1.val+localctx.e2.val
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None
            self._INT = None # Token
            self._expr = None # ExprContext

        def INT(self):
            return self.getToken(Arit1Parser.INT, 0)

        def expr(self):
            return self.getTypedRuleContext(Arit1Parser.ExprContext,0)


        def getRuleIndex(self):
            return Arit1Parser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = Arit1Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Arit1Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                localctx._INT = self.match(Arit1Parser.INT)
                localctx.val = int((None if localctx._INT is None else localctx._INT.text))
                pass
            elif token in [Arit1Parser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(Arit1Parser.T__0)
                self.state = 41
                localctx._expr = self.expr(0)
                self.state = 42
                self.match(Arit1Parser.T__1)
                localctx.val=localctx._expr.val
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




