# Generated from ArithmeticGrammar.g4 by ANTLR 4.12.0
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
        4,1,11,44,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,31,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,39,8,2,10,
        2,12,2,42,9,2,1,2,0,1,4,3,0,2,4,0,2,1,0,1,2,1,0,3,4,47,0,6,1,0,0,
        0,2,19,1,0,0,0,4,30,1,0,0,0,6,11,3,2,1,0,7,8,5,11,0,0,8,10,3,2,1,
        0,9,7,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,0,
        0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,1,0,0,0,16,18,3,4,2,0,17,16,
        1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,3,1,0,0,0,21,
        19,1,0,0,0,22,23,6,2,-1,0,23,31,5,9,0,0,24,25,5,5,0,0,25,26,3,4,
        2,0,26,27,5,6,0,0,27,31,1,0,0,0,28,31,5,7,0,0,29,31,5,8,0,0,30,22,
        1,0,0,0,30,24,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,40,1,0,0,0,
        32,33,10,6,0,0,33,34,7,0,0,0,34,39,3,4,2,7,35,36,10,5,0,0,36,37,
        7,1,0,0,37,39,3,4,2,6,38,32,1,0,0,0,38,35,1,0,0,0,39,42,1,0,0,0,
        40,38,1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,40,1,0,0,0,5,11,19,30,
        38,40
    ]

class ArithmeticGrammarParser ( Parser ):

    grammarFileName = "ArithmeticGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "HELLO", "BYE", 
                      "INT", "WS", "NL" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "line", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    HELLO=7
    BYE=8
    INT=9
    WS=10
    NL=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticGrammarParser.LineContext)
            else:
                return self.getTypedRuleContext(ArithmeticGrammarParser.LineContext,i)


        def EOF(self):
            return self.getToken(ArithmeticGrammarParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticGrammarParser.NL)
            else:
                return self.getToken(ArithmeticGrammarParser.NL, i)

        def getRuleIndex(self):
            return ArithmeticGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ArithmeticGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.line()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 7
                self.match(ArithmeticGrammarParser.NL)
                self.state = 8
                self.line()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(ArithmeticGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticGrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return ArithmeticGrammarParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = ArithmeticGrammarParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 928) != 0):
                self.state = 16
                self.expr(0)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticGrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ArithmeticGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ByeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticGrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def BYE(self):
            return self.getToken(ArithmeticGrammarParser.BYE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterByeExpr" ):
                listener.enterByeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitByeExpr" ):
                listener.exitByeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByeExpr" ):
                return visitor.visitByeExpr(self)
            else:
                return visitor.visitChildren(self)


    class HelloExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticGrammarParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def HELLO(self):
            return self.getToken(ArithmeticGrammarParser.HELLO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelloExpr" ):
                listener.enterHelloExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelloExpr" ):
                listener.exitHelloExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelloExpr" ):
                return visitor.visitHelloExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticGrammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticGrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = ArithmeticGrammarParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                localctx.atom = self.match(ArithmeticGrammarParser.INT)
                pass
            elif token in [5]:
                localctx = ArithmeticGrammarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(ArithmeticGrammarParser.T__4)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(ArithmeticGrammarParser.T__5)
                pass
            elif token in [7]:
                localctx = ArithmeticGrammarParser.HelloExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                localctx.atom = self.match(ArithmeticGrammarParser.HELLO)
                pass
            elif token in [8]:
                localctx = ArithmeticGrammarParser.ByeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                localctx.atom = self.match(ArithmeticGrammarParser.BYE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticGrammarParser.InfixExprContext(self, ArithmeticGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 33
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticGrammarParser.InfixExprContext(self, ArithmeticGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




