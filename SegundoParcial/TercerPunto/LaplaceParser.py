# Generated from Laplace.g4 by ANTLR 4.13.2
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
        4,1,16,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,3,0,12,8,0,
        1,0,1,0,1,0,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,72,
        8,3,10,3,12,3,75,9,3,1,3,1,3,1,3,0,2,0,2,4,0,2,4,6,0,1,1,0,14,15,
        85,0,11,1,0,0,0,2,24,1,0,0,0,4,63,1,0,0,0,6,65,1,0,0,0,8,9,6,0,-1,
        0,9,12,3,6,3,0,10,12,3,2,1,0,11,8,1,0,0,0,11,10,1,0,0,0,12,21,1,
        0,0,0,13,14,10,3,0,0,14,15,5,3,0,0,15,20,3,2,1,0,16,17,10,2,0,0,
        17,18,5,4,0,0,18,20,3,2,1,0,19,13,1,0,0,0,19,16,1,0,0,0,20,23,1,
        0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,21,1,0,0,0,24,
        25,6,1,-1,0,25,26,3,4,2,0,26,35,1,0,0,0,27,28,10,3,0,0,28,29,5,5,
        0,0,29,34,3,4,2,0,30,31,10,2,0,0,31,32,5,6,0,0,32,34,3,4,2,0,33,
        27,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,
        0,36,3,1,0,0,0,37,35,1,0,0,0,38,64,5,15,0,0,39,40,5,10,0,0,40,41,
        5,1,0,0,41,42,5,7,0,0,42,43,5,4,0,0,43,44,7,0,0,0,44,45,5,5,0,0,
        45,46,5,14,0,0,46,64,5,8,0,0,47,48,5,11,0,0,48,49,5,7,0,0,49,50,
        5,15,0,0,50,51,5,5,0,0,51,52,5,14,0,0,52,64,5,8,0,0,53,54,5,14,0,
        0,54,55,5,7,0,0,55,56,3,0,0,0,56,57,5,8,0,0,57,64,1,0,0,0,58,64,
        5,14,0,0,59,60,5,7,0,0,60,61,3,0,0,0,61,62,5,8,0,0,62,64,1,0,0,0,
        63,38,1,0,0,0,63,39,1,0,0,0,63,47,1,0,0,0,63,53,1,0,0,0,63,58,1,
        0,0,0,63,59,1,0,0,0,64,5,1,0,0,0,65,66,5,9,0,0,66,67,5,12,0,0,67,
        68,5,13,0,0,68,73,3,4,2,0,69,70,5,5,0,0,70,72,3,4,2,0,71,69,1,0,
        0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,
        1,0,0,0,76,77,5,2,0,0,77,7,1,0,0,0,7,11,19,21,33,35,63,73
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'dt'", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "'int'", "'e'", "'sin'", "'0'", "'infinity'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "MUL", "DIV", "LPAREN", "RPAREN", "INTEGRAL", "EXP", 
                      "SIN", "LIMIT_FROM", "LIMIT_TO", "ID", "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_integral = 3

    ruleNames =  [ "expr", "term", "factor", "integral" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    PLUS=3
    MINUS=4
    MUL=5
    DIV=6
    LPAREN=7
    RPAREN=8
    INTEGRAL=9
    EXP=10
    SIN=11
    LIMIT_FROM=12
    LIMIT_TO=13
    ID=14
    NUMBER=15
    WS=16

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
            return LaplaceParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(LaplaceParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpr" ):
                listener.enterTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpr" ):
                listener.exitTermExpr(self)


    class LaplaceTransformContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def integral(self):
            return self.getTypedRuleContext(LaplaceParser.IntegralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaplaceTransform" ):
                listener.enterLaplaceTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaplaceTransform" ):
                listener.exitLaplaceTransform(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(LaplaceParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(LaplaceParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(LaplaceParser.PLUS, 0)
        def term(self):
            return self.getTypedRuleContext(LaplaceParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaplaceParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = LaplaceParser.LaplaceTransformContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 9
                self.integral()
                pass
            elif token in [7, 10, 11, 14, 15]:
                localctx = LaplaceParser.TermExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.term(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 19
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LaplaceParser.AddExprContext(self, LaplaceParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 13
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 14
                        self.match(LaplaceParser.PLUS)
                        self.state = 15
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = LaplaceParser.SubExprContext(self, LaplaceParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 17
                        self.match(LaplaceParser.MINUS)
                        self.state = 18
                        self.term(0)
                        pass

             
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            return LaplaceParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulExprContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(LaplaceParser.TermContext,0)

        def MUL(self):
            return self.getToken(LaplaceParser.MUL, 0)
        def factor(self):
            return self.getTypedRuleContext(LaplaceParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)


    class DivExprContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(LaplaceParser.TermContext,0)

        def DIV(self):
            return self.getToken(LaplaceParser.DIV, 0)
        def factor(self):
            return self.getTypedRuleContext(LaplaceParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)


    class FactorExprContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(LaplaceParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorExpr" ):
                listener.enterFactorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorExpr" ):
                listener.exitFactorExpr(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaplaceParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = LaplaceParser.FactorExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 25
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LaplaceParser.MulExprContext(self, LaplaceParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 27
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 28
                        self.match(LaplaceParser.MUL)
                        self.state = 29
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = LaplaceParser.DivExprContext(self, LaplaceParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 30
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 31
                        self.match(LaplaceParser.DIV)
                        self.state = 32
                        self.factor()
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            return LaplaceParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SinFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(LaplaceParser.SIN, 0)
        def LPAREN(self):
            return self.getToken(LaplaceParser.LPAREN, 0)
        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)
        def MUL(self):
            return self.getToken(LaplaceParser.MUL, 0)
        def ID(self):
            return self.getToken(LaplaceParser.ID, 0)
        def RPAREN(self):
            return self.getToken(LaplaceParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinFactor" ):
                listener.enterSinFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinFactor" ):
                listener.exitSinFactor(self)


    class VariableFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LaplaceParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableFactor" ):
                listener.enterVariableFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableFactor" ):
                listener.exitVariableFactor(self)


    class NumberFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberFactor" ):
                listener.enterNumberFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberFactor" ):
                listener.exitNumberFactor(self)


    class ParenExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LaplaceParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(LaplaceParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class ExpFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXP(self):
            return self.getToken(LaplaceParser.EXP, 0)
        def LPAREN(self):
            return self.getToken(LaplaceParser.LPAREN, 0)
        def MINUS(self):
            return self.getToken(LaplaceParser.MINUS, 0)
        def MUL(self):
            return self.getToken(LaplaceParser.MUL, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceParser.ID)
            else:
                return self.getToken(LaplaceParser.ID, i)
        def RPAREN(self):
            return self.getToken(LaplaceParser.RPAREN, 0)
        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpFactor" ):
                listener.enterExpFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpFactor" ):
                listener.exitExpFactor(self)


    class FuncFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LaplaceParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LaplaceParser.ID, 0)
        def LPAREN(self):
            return self.getToken(LaplaceParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LaplaceParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(LaplaceParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncFactor" ):
                listener.enterFuncFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncFactor" ):
                listener.exitFuncFactor(self)



    def factor(self):

        localctx = LaplaceParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = LaplaceParser.NumberFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(LaplaceParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = LaplaceParser.ExpFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(LaplaceParser.EXP)
                self.state = 40
                self.match(LaplaceParser.T__0)
                self.state = 41
                self.match(LaplaceParser.LPAREN)
                self.state = 42
                self.match(LaplaceParser.MINUS)
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(LaplaceParser.MUL)
                self.state = 45
                self.match(LaplaceParser.ID)
                self.state = 46
                self.match(LaplaceParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = LaplaceParser.SinFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.match(LaplaceParser.SIN)
                self.state = 48
                self.match(LaplaceParser.LPAREN)
                self.state = 49
                self.match(LaplaceParser.NUMBER)
                self.state = 50
                self.match(LaplaceParser.MUL)
                self.state = 51
                self.match(LaplaceParser.ID)
                self.state = 52
                self.match(LaplaceParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = LaplaceParser.FuncFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.match(LaplaceParser.ID)
                self.state = 54
                self.match(LaplaceParser.LPAREN)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(LaplaceParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = LaplaceParser.VariableFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.match(LaplaceParser.ID)
                pass

            elif la_ == 6:
                localctx = LaplaceParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.match(LaplaceParser.LPAREN)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(LaplaceParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGRAL(self):
            return self.getToken(LaplaceParser.INTEGRAL, 0)

        def LIMIT_FROM(self):
            return self.getToken(LaplaceParser.LIMIT_FROM, 0)

        def LIMIT_TO(self):
            return self.getToken(LaplaceParser.LIMIT_TO, 0)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.FactorContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceParser.MUL)
            else:
                return self.getToken(LaplaceParser.MUL, i)

        def getRuleIndex(self):
            return LaplaceParser.RULE_integral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral" ):
                listener.enterIntegral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral" ):
                listener.exitIntegral(self)




    def integral(self):

        localctx = LaplaceParser.IntegralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_integral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(LaplaceParser.INTEGRAL)
            self.state = 66
            self.match(LaplaceParser.LIMIT_FROM)
            self.state = 67
            self.match(LaplaceParser.LIMIT_TO)
            self.state = 68
            self.factor()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 69
                self.match(LaplaceParser.MUL)
                self.state = 70
                self.factor()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(LaplaceParser.T__1)
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




