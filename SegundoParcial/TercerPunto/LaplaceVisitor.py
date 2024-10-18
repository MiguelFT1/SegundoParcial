# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceParser.

class LaplaceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceParser#TermExpr.
    def visitTermExpr(self, ctx:LaplaceParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#LaplaceTransform.
    def visitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#SubExpr.
    def visitSubExpr(self, ctx:LaplaceParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#AddExpr.
    def visitAddExpr(self, ctx:LaplaceParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#MulExpr.
    def visitMulExpr(self, ctx:LaplaceParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#DivExpr.
    def visitDivExpr(self, ctx:LaplaceParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#FactorExpr.
    def visitFactorExpr(self, ctx:LaplaceParser.FactorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#NumberFactor.
    def visitNumberFactor(self, ctx:LaplaceParser.NumberFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#ExpFactor.
    def visitExpFactor(self, ctx:LaplaceParser.ExpFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#FuncFactor.
    def visitFuncFactor(self, ctx:LaplaceParser.FuncFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#VariableFactor.
    def visitVariableFactor(self, ctx:LaplaceParser.VariableFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#ParenExpr.
    def visitParenExpr(self, ctx:LaplaceParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#integral.
    def visitIntegral(self, ctx:LaplaceParser.IntegralContext):
        return self.visitChildren(ctx)



del LaplaceParser