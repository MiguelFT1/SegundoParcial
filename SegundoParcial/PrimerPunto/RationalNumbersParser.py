# Generated from RationalNumbers.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,0,
        5,0,15,8,0,10,0,12,0,18,9,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,26,8,1,10,
        1,12,1,29,9,1,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,
        0,2,0,2,4,0,2,4,6,0,2,1,0,2,3,1,0,4,5,40,0,8,1,0,0,0,2,19,1,0,0,
        0,4,35,1,0,0,0,6,37,1,0,0,0,8,9,6,0,-1,0,9,10,3,2,1,0,10,16,1,0,
        0,0,11,12,10,2,0,0,12,13,7,0,0,0,13,15,3,2,1,0,14,11,1,0,0,0,15,
        18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,1,1,0,0,0,18,16,1,0,0,
        0,19,20,6,1,-1,0,20,21,3,4,2,0,21,27,1,0,0,0,22,23,10,2,0,0,23,24,
        7,1,0,0,24,26,3,4,2,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,3,1,0,0,0,29,27,1,0,0,0,30,36,3,6,3,0,31,32,5,6,
        0,0,32,33,3,0,0,0,33,34,5,7,0,0,34,36,1,0,0,0,35,30,1,0,0,0,35,31,
        1,0,0,0,36,5,1,0,0,0,37,38,5,1,0,0,38,39,5,5,0,0,39,40,5,1,0,0,40,
        7,1,0,0,0,3,16,27,35
    ]

class RationalNumbersParser ( Parser ):

    grammarFileName = "RationalNumbers.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NUM", "PLUS", "MINUS", "MULT", "DIV", 
                      "LPAREN", "RPAREN", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_rational = 3

    ruleNames =  [ "expr", "term", "factor", "rational" ]

    EOF = Token.EOF
    NUM=1
    PLUS=2
    MINUS=3
    MULT=4
    DIV=5
    LPAREN=6
    RPAREN=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RationalNumbersParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RationalNumbersParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(RationalNumbersParser.TermContext,0)

        def PLUS(self):
            return self.getToken(RationalNumbersParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(RationalNumbersParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ToTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RationalNumbersParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToTerm" ):
                listener.enterToTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToTerm" ):
                listener.exitToTerm(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RationalNumbersParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RationalNumbersParser.ToTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 9
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RationalNumbersParser.AddSubContext(self, RationalNumbersParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 11
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 12
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 13
                    self.term(0) 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RationalNumbersParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(RationalNumbersParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToFactor" ):
                listener.enterToFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToFactor" ):
                listener.exitToFactor(self)


    class MulDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.TermContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RationalNumbersParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(RationalNumbersParser.FactorContext,0)

        def MULT(self):
            return self.getToken(RationalNumbersParser.MULT, 0)
        def DIV(self):
            return self.getToken(RationalNumbersParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RationalNumbersParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RationalNumbersParser.ToFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 20
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RationalNumbersParser.MulDivContext(self, RationalNumbersParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 22
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 23
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==4 or _la==5):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 24
                    self.factor() 
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RationalNumbersParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RationalNumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rational(self):
            return self.getTypedRuleContext(RationalNumbersParser.RationalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRationalNumber" ):
                listener.enterRationalNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRationalNumber" ):
                listener.exitRationalNumber(self)


    class ParenthesesContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RationalNumbersParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(RationalNumbersParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(RationalNumbersParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)



    def factor(self):

        localctx = RationalNumbersParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = RationalNumbersParser.RationalNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.rational()
                pass
            elif token in [6]:
                localctx = RationalNumbersParser.ParenthesesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(RationalNumbersParser.LPAREN)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(RationalNumbersParser.RPAREN)
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


    class RationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RationalNumbersParser.RULE_rational

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FractionContext(RationalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalNumbersParser.RationalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(RationalNumbersParser.NUM)
            else:
                return self.getToken(RationalNumbersParser.NUM, i)
        def DIV(self):
            return self.getToken(RationalNumbersParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFraction" ):
                listener.enterFraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFraction" ):
                listener.exitFraction(self)



    def rational(self):

        localctx = RationalNumbersParser.RationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rational)
        try:
            localctx = RationalNumbersParser.FractionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(RationalNumbersParser.NUM)
            self.state = 38
            self.match(RationalNumbersParser.DIV)
            self.state = 39
            self.match(RationalNumbersParser.NUM)
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
        self._predicates[0] = self.expr_sempred
        self._predicates[1] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




