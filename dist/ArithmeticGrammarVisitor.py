# Generated from ArithmeticGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArithmeticGrammarParser import ArithmeticGrammarParser
else:
    from ArithmeticGrammarParser import ArithmeticGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticGrammarParser.

class ArithmeticGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticGrammarParser#prog.
    def visitProg(self, ctx:ArithmeticGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticGrammarParser#line.
    def visitLine(self, ctx:ArithmeticGrammarParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticGrammarParser#NumberExpr.
    def visitNumberExpr(self, ctx:ArithmeticGrammarParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticGrammarParser#ByeExpr.
    def visitByeExpr(self, ctx:ArithmeticGrammarParser.ByeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticGrammarParser#HelloExpr.
    def visitHelloExpr(self, ctx:ArithmeticGrammarParser.HelloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticGrammarParser#ParenExpr.
    def visitParenExpr(self, ctx:ArithmeticGrammarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticGrammarParser#InfixExpr.
    def visitInfixExpr(self, ctx:ArithmeticGrammarParser.InfixExprContext):
        return self.visitChildren(ctx)



del ArithmeticGrammarParser