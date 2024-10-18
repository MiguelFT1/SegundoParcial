# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#TermExpr.
    def enterTermExpr(self, ctx:LaplaceParser.TermExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#TermExpr.
    def exitTermExpr(self, ctx:LaplaceParser.TermExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#LaplaceTransform.
    def enterLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass

    # Exit a parse tree produced by LaplaceParser#LaplaceTransform.
    def exitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass


    # Enter a parse tree produced by LaplaceParser#SubExpr.
    def enterSubExpr(self, ctx:LaplaceParser.SubExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#SubExpr.
    def exitSubExpr(self, ctx:LaplaceParser.SubExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#AddExpr.
    def enterAddExpr(self, ctx:LaplaceParser.AddExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#AddExpr.
    def exitAddExpr(self, ctx:LaplaceParser.AddExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#MulExpr.
    def enterMulExpr(self, ctx:LaplaceParser.MulExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#MulExpr.
    def exitMulExpr(self, ctx:LaplaceParser.MulExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#DivExpr.
    def enterDivExpr(self, ctx:LaplaceParser.DivExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#DivExpr.
    def exitDivExpr(self, ctx:LaplaceParser.DivExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#FactorExpr.
    def enterFactorExpr(self, ctx:LaplaceParser.FactorExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#FactorExpr.
    def exitFactorExpr(self, ctx:LaplaceParser.FactorExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#NumberFactor.
    def enterNumberFactor(self, ctx:LaplaceParser.NumberFactorContext):
        pass

    # Exit a parse tree produced by LaplaceParser#NumberFactor.
    def exitNumberFactor(self, ctx:LaplaceParser.NumberFactorContext):
        pass


    # Enter a parse tree produced by LaplaceParser#ExpFactor.
    def enterExpFactor(self, ctx:LaplaceParser.ExpFactorContext):
        pass

    # Exit a parse tree produced by LaplaceParser#ExpFactor.
    def exitExpFactor(self, ctx:LaplaceParser.ExpFactorContext):
        pass


    # Enter a parse tree produced by LaplaceParser#SinFactor.
    def enterSinFactor(self, ctx:LaplaceParser.SinFactorContext):
        pass

    # Exit a parse tree produced by LaplaceParser#SinFactor.
    def exitSinFactor(self, ctx:LaplaceParser.SinFactorContext):
        pass


    # Enter a parse tree produced by LaplaceParser#FuncFactor.
    def enterFuncFactor(self, ctx:LaplaceParser.FuncFactorContext):
        pass

    # Exit a parse tree produced by LaplaceParser#FuncFactor.
    def exitFuncFactor(self, ctx:LaplaceParser.FuncFactorContext):
        pass


    # Enter a parse tree produced by LaplaceParser#VariableFactor.
    def enterVariableFactor(self, ctx:LaplaceParser.VariableFactorContext):
        pass

    # Exit a parse tree produced by LaplaceParser#VariableFactor.
    def exitVariableFactor(self, ctx:LaplaceParser.VariableFactorContext):
        pass


    # Enter a parse tree produced by LaplaceParser#ParenExpr.
    def enterParenExpr(self, ctx:LaplaceParser.ParenExprContext):
        pass

    # Exit a parse tree produced by LaplaceParser#ParenExpr.
    def exitParenExpr(self, ctx:LaplaceParser.ParenExprContext):
        pass


    # Enter a parse tree produced by LaplaceParser#integral.
    def enterIntegral(self, ctx:LaplaceParser.IntegralContext):
        pass

    # Exit a parse tree produced by LaplaceParser#integral.
    def exitIntegral(self, ctx:LaplaceParser.IntegralContext):
        pass



del LaplaceParser