# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,96,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        13,4,13,73,8,13,11,13,12,13,74,1,14,4,14,78,8,14,11,14,12,14,79,
        1,14,1,14,4,14,84,8,14,11,14,12,14,85,3,14,88,8,14,1,15,4,15,91,
        8,15,11,15,12,15,92,1,15,1,15,0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,1,0,3,2,0,
        65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,100,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,
        0,0,0,3,35,1,0,0,0,5,38,1,0,0,0,7,40,1,0,0,0,9,42,1,0,0,0,11,44,
        1,0,0,0,13,46,1,0,0,0,15,48,1,0,0,0,17,50,1,0,0,0,19,54,1,0,0,0,
        21,56,1,0,0,0,23,60,1,0,0,0,25,62,1,0,0,0,27,72,1,0,0,0,29,77,1,
        0,0,0,31,90,1,0,0,0,33,34,5,94,0,0,34,2,1,0,0,0,35,36,5,100,0,0,
        36,37,5,116,0,0,37,4,1,0,0,0,38,39,5,43,0,0,39,6,1,0,0,0,40,41,5,
        45,0,0,41,8,1,0,0,0,42,43,5,42,0,0,43,10,1,0,0,0,44,45,5,47,0,0,
        45,12,1,0,0,0,46,47,5,40,0,0,47,14,1,0,0,0,48,49,5,41,0,0,49,16,
        1,0,0,0,50,51,5,105,0,0,51,52,5,110,0,0,52,53,5,116,0,0,53,18,1,
        0,0,0,54,55,5,101,0,0,55,20,1,0,0,0,56,57,5,115,0,0,57,58,5,105,
        0,0,58,59,5,110,0,0,59,22,1,0,0,0,60,61,5,48,0,0,61,24,1,0,0,0,62,
        63,5,105,0,0,63,64,5,110,0,0,64,65,5,102,0,0,65,66,5,105,0,0,66,
        67,5,110,0,0,67,68,5,105,0,0,68,69,5,116,0,0,69,70,5,121,0,0,70,
        26,1,0,0,0,71,73,7,0,0,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,
        0,74,75,1,0,0,0,75,28,1,0,0,0,76,78,7,1,0,0,77,76,1,0,0,0,78,79,
        1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,87,1,0,0,0,81,83,5,46,0,0,
        82,84,7,1,0,0,83,82,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,
        0,0,0,86,88,1,0,0,0,87,81,1,0,0,0,87,88,1,0,0,0,88,30,1,0,0,0,89,
        91,7,2,0,0,90,89,1,0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,
        0,93,94,1,0,0,0,94,95,6,15,0,0,95,32,1,0,0,0,6,0,74,79,85,87,92,
        1,6,0,0
    ]

class LaplaceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    PLUS = 3
    MINUS = 4
    MUL = 5
    DIV = 6
    LPAREN = 7
    RPAREN = 8
    INTEGRAL = 9
    EXP = 10
    SIN = 11
    LIMIT_FROM = 12
    LIMIT_TO = 13
    ID = 14
    NUMBER = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'^'", "'dt'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'int'", 
            "'e'", "'sin'", "'0'", "'infinity'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "LPAREN", "RPAREN", "INTEGRAL", 
            "EXP", "SIN", "LIMIT_FROM", "LIMIT_TO", "ID", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", 
                  "RPAREN", "INTEGRAL", "EXP", "SIN", "LIMIT_FROM", "LIMIT_TO", 
                  "ID", "NUMBER", "WS" ]

    grammarFileName = "Laplace.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


