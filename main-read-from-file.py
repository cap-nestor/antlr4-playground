import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.ArithmeticGrammarLexer import ArithmeticGrammarLexer
from dist.ArithmeticGrammarParser import ArithmeticGrammarParser
from dist.ArithmeticGrammarVisitor import ArithmeticGrammarVisitor


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

  
class MyVisitor(ArithmeticGrammarVisitor):
    def visitNumberExpr(self, ctx):
        print(">>> Reading a number:" + str(ctx.getText()))
        value = ctx.getText()
        return int(value)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        print(">>> Evaluating Math Operation "+str(ctx.op.text)+" with "+str(l)+" and "+str(r))
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
        print(">>> Evaluating Hello")
        return (f"{ctx.getText()} {get_username()}")


def main(argv):
    # Get the file to parse as the first parameter
    # i.e. $ python3 main-read-from-file.py commands.txt 
    data =  FileStream(argv[1])
    # lexer
    lexer = ArithmeticGrammarLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = ArithmeticGrammarParser(stream)
    # Invoke the name of the biggest parser block
    tree = parser.prog()
    # Evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    print(output)
    # This should print a decision tree, but it is not working
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)