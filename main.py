import sys
from antlr4 import *
from dist.ArithmeticGrammarLexer import ArithmeticGrammarLexer
from dist.ArithmeticGrammarParser import ArithmeticGrammarParser
from dist.ArithmeticGrammarVisitor import ArithmeticGrammarVisitor


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

  
class MyVisitor(ArithmeticGrammarVisitor):
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()} {get_username()}")


if __name__ == "__main__":
    while 1:
        data =  InputStream(input(">>> "))
        # lexer
        lexer = ArithmeticGrammarLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = ArithmeticGrammarParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
