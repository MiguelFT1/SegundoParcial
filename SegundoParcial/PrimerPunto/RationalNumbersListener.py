# Generated from RationalNumbers.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RationalNumbersParser import RationalNumbersParser
else:
    from RationalNumbersParser import RationalNumbersParser

# This class defines a complete listener for a parse tree produced by RationalNumbersParser.
class RationalNumbersListener(ParseTreeListener):

    # Enter a parse tree produced by RationalNumbersParser#AddSub.
    def enterAddSub(self, ctx:RationalNumbersParser.AddSubContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#AddSub.
    def exitAddSub(self, ctx:RationalNumbersParser.AddSubContext):
        pass


    # Enter a parse tree produced by RationalNumbersParser#ToTerm.
    def enterToTerm(self, ctx:RationalNumbersParser.ToTermContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#ToTerm.
    def exitToTerm(self, ctx:RationalNumbersParser.ToTermContext):
        pass


    # Enter a parse tree produced by RationalNumbersParser#ToFactor.
    def enterToFactor(self, ctx:RationalNumbersParser.ToFactorContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#ToFactor.
    def exitToFactor(self, ctx:RationalNumbersParser.ToFactorContext):
        pass


    # Enter a parse tree produced by RationalNumbersParser#MulDiv.
    def enterMulDiv(self, ctx:RationalNumbersParser.MulDivContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#MulDiv.
    def exitMulDiv(self, ctx:RationalNumbersParser.MulDivContext):
        pass


    # Enter a parse tree produced by RationalNumbersParser#RationalNumber.
    def enterRationalNumber(self, ctx:RationalNumbersParser.RationalNumberContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#RationalNumber.
    def exitRationalNumber(self, ctx:RationalNumbersParser.RationalNumberContext):
        pass


    # Enter a parse tree produced by RationalNumbersParser#Parentheses.
    def enterParentheses(self, ctx:RationalNumbersParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#Parentheses.
    def exitParentheses(self, ctx:RationalNumbersParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by RationalNumbersParser#Fraction.
    def enterFraction(self, ctx:RationalNumbersParser.FractionContext):
        pass

    # Exit a parse tree produced by RationalNumbersParser#Fraction.
    def exitFraction(self, ctx:RationalNumbersParser.FractionContext):
        pass



del RationalNumbersParser