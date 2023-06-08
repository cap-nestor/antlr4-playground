# Generated from ArithmeticGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArithmeticGrammarParser import ArithmeticGrammarParser
else:
    from ArithmeticGrammarParser import ArithmeticGrammarParser

# This class defines a complete listener for a parse tree produced by ArithmeticGrammarParser.
class ArithmeticGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticGrammarParser#prog.
    def enterProg(self, ctx:ArithmeticGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#prog.
    def exitProg(self, ctx:ArithmeticGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#line.
    def enterLine(self, ctx:ArithmeticGrammarParser.LineContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#line.
    def exitLine(self, ctx:ArithmeticGrammarParser.LineContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#NumberExpr.
    def enterNumberExpr(self, ctx:ArithmeticGrammarParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#NumberExpr.
    def exitNumberExpr(self, ctx:ArithmeticGrammarParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#ByeExpr.
    def enterByeExpr(self, ctx:ArithmeticGrammarParser.ByeExprContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#ByeExpr.
    def exitByeExpr(self, ctx:ArithmeticGrammarParser.ByeExprContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#HelloExpr.
    def enterHelloExpr(self, ctx:ArithmeticGrammarParser.HelloExprContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#HelloExpr.
    def exitHelloExpr(self, ctx:ArithmeticGrammarParser.HelloExprContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#ParenExpr.
    def enterParenExpr(self, ctx:ArithmeticGrammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#ParenExpr.
    def exitParenExpr(self, ctx:ArithmeticGrammarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ArithmeticGrammarParser#InfixExpr.
    def enterInfixExpr(self, ctx:ArithmeticGrammarParser.InfixExprContext):
        pass

    # Exit a parse tree produced by ArithmeticGrammarParser#InfixExpr.
    def exitInfixExpr(self, ctx:ArithmeticGrammarParser.InfixExprContext):
        pass



del ArithmeticGrammarParser