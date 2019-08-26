# Generated from grammar.g4 by ANTLR 4.11.2-SNAPSHOT
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
        4,1,19,182,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,68,8,
        0,1,1,3,1,71,8,1,1,2,3,2,74,8,2,1,3,1,3,1,3,1,4,4,4,80,8,4,11,4,
        12,4,81,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,5,7,93,8,7,10,7,12,7,
        96,9,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,11,4,11,108,8,11,
        11,11,12,11,109,1,12,1,12,1,13,1,13,1,13,3,13,117,8,13,1,14,1,14,
        3,14,121,8,14,1,15,4,15,124,8,15,11,15,12,15,125,1,16,4,16,129,8,
        16,11,16,12,16,130,1,17,4,17,134,8,17,11,17,12,17,135,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,3,20,148,8,20,1,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,25,1,25,1,25,1,26,5,26,169,8,26,10,26,12,26,172,9,26,1,27,1,27,
        1,27,1,27,1,28,1,28,3,28,180,8,28,1,28,0,0,29,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,
        2,2,0,4,4,15,15,4,0,1,4,7,7,12,13,15,15,167,0,58,1,0,0,0,2,70,1,
        0,0,0,4,73,1,0,0,0,6,75,1,0,0,0,8,79,1,0,0,0,10,83,1,0,0,0,12,88,
        1,0,0,0,14,94,1,0,0,0,16,97,1,0,0,0,18,100,1,0,0,0,20,104,1,0,0,
        0,22,107,1,0,0,0,24,111,1,0,0,0,26,116,1,0,0,0,28,120,1,0,0,0,30,
        123,1,0,0,0,32,128,1,0,0,0,34,133,1,0,0,0,36,137,1,0,0,0,38,141,
        1,0,0,0,40,147,1,0,0,0,42,149,1,0,0,0,44,153,1,0,0,0,46,158,1,0,
        0,0,48,161,1,0,0,0,50,164,1,0,0,0,52,170,1,0,0,0,54,173,1,0,0,0,
        56,179,1,0,0,0,58,59,3,2,1,0,59,60,5,1,0,0,60,61,5,5,0,0,61,62,3,
        4,2,0,62,63,3,56,28,0,63,64,5,5,0,0,64,65,3,22,11,0,65,67,3,8,4,
        0,66,68,5,5,0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,1,1,0,0,0,69,71,3,
        48,24,0,70,69,1,0,0,0,70,71,1,0,0,0,71,3,1,0,0,0,72,74,3,10,5,0,
        73,72,1,0,0,0,73,74,1,0,0,0,74,5,1,0,0,0,75,76,5,5,0,0,76,77,3,22,
        11,0,77,7,1,0,0,0,78,80,3,6,3,0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,9,1,0,0,0,83,84,5,8,0,0,84,85,3,12,6,0,
        85,86,5,9,0,0,86,87,5,5,0,0,87,11,1,0,0,0,88,89,3,18,9,0,89,90,3,
        14,7,0,90,13,1,0,0,0,91,93,3,16,8,0,92,91,1,0,0,0,93,96,1,0,0,0,
        94,92,1,0,0,0,94,95,1,0,0,0,95,15,1,0,0,0,96,94,1,0,0,0,97,98,5,
        14,0,0,98,99,3,18,9,0,99,17,1,0,0,0,100,101,5,2,0,0,101,102,5,10,
        0,0,102,103,3,30,15,0,103,19,1,0,0,0,104,105,7,0,0,0,105,21,1,0,
        0,0,106,108,3,20,10,0,107,106,1,0,0,0,108,109,1,0,0,0,109,107,1,
        0,0,0,109,110,1,0,0,0,110,23,1,0,0,0,111,112,7,1,0,0,112,25,1,0,
        0,0,113,117,5,19,0,0,114,117,3,24,12,0,115,117,5,10,0,0,116,113,
        1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,27,1,0,0,0,118,121,3,
        26,13,0,119,121,5,9,0,0,120,118,1,0,0,0,120,119,1,0,0,0,121,29,1,
        0,0,0,122,124,3,24,12,0,123,122,1,0,0,0,124,125,1,0,0,0,125,123,
        1,0,0,0,125,126,1,0,0,0,126,31,1,0,0,0,127,129,3,26,13,0,128,127,
        1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,33,1,
        0,0,0,132,134,3,28,14,0,133,132,1,0,0,0,134,135,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,35,1,0,0,0,137,138,5,16,0,0,138,139,
        3,32,16,0,139,140,5,16,0,0,140,37,1,0,0,0,141,142,5,17,0,0,142,143,
        3,32,16,0,143,144,5,17,0,0,144,39,1,0,0,0,145,148,3,36,18,0,146,
        148,3,38,19,0,147,145,1,0,0,0,147,146,1,0,0,0,148,41,1,0,0,0,149,
        150,5,8,0,0,150,151,3,40,20,0,151,152,5,9,0,0,152,43,1,0,0,0,153,
        154,5,3,0,0,154,155,5,13,0,0,155,156,3,42,21,0,156,157,3,34,17,0,
        157,45,1,0,0,0,158,159,5,4,0,0,159,160,3,52,26,0,160,47,1,0,0,0,
        161,162,5,11,0,0,162,163,5,5,0,0,163,49,1,0,0,0,164,165,5,12,0,0,
        165,166,5,4,0,0,166,51,1,0,0,0,167,169,3,50,25,0,168,167,1,0,0,0,
        169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,53,1,0,0,0,172,
        170,1,0,0,0,173,174,3,46,23,0,174,175,5,13,0,0,175,176,3,34,17,0,
        176,55,1,0,0,0,177,180,3,44,22,0,178,180,3,54,27,0,179,177,1,0,0,
        0,179,178,1,0,0,0,180,57,1,0,0,0,14,67,70,73,81,94,109,116,120,125,
        130,135,147,170,179
    ]

class apt_sourceParser ( Parser ):

    grammarFileName = "grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'cdrom:'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'='", "'#'", "'+'", "':'", "','", "'-'", 
                     "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>", "TypeR", "OptionName", "CdromSchema", 
                      "Word", "WSS", "WS", "PunctuationAllowedInOptionValue", 
                      "OptionsStart", "OptionsEnd", "OptionNameValueSeparator", 
                      "CommentMarker", "Plus", "Colon", "OptionsSeparator", 
                      "Dash", "SingleTick", "DoubleTick", "WordChar", "NonWhitespaceNonOptionValueNonSquareRightBracketNonEq" ]

    RULE_record = 0
    RULE_commenterR_opt_our = 1
    RULE_optionsR_opt_our = 2
    RULE_component = 3
    RULE_componentsR = 4
    RULE_optionsR = 5
    RULE_optionsList = 6
    RULE_additionalOptions = 7
    RULE_additionalOption = 8
    RULE_optionR = 9
    RULE_wordWithDashSegment = 10
    RULE_wordWithDash = 11
    RULE_optionValueSegment = 12
    RULE_nonSquareBracketStringSegment = 13
    RULE_nonSpaceStringSegment = 14
    RULE_optionValue = 15
    RULE_nonSquareBracketString = 16
    RULE_nonSpaceString = 17
    RULE_singleTickEnclosedString = 18
    RULE_doubleTickEnclosedString = 19
    RULE_tickEnclosedString = 20
    RULE_enclosedString = 21
    RULE_cdromURI = 22
    RULE_uriSchema = 23
    RULE_commenterR = 24
    RULE_wordWithPlus = 25
    RULE_restSchemaWords = 26
    RULE_genericURI = 27
    RULE_uriR = 28

    ruleNames =  [ "record", "commenterR_opt_our", "optionsR_opt_our", "component", 
                   "componentsR", "optionsR", "optionsList", "additionalOptions", 
                   "additionalOption", "optionR", "wordWithDashSegment", 
                   "wordWithDash", "optionValueSegment", "nonSquareBracketStringSegment", 
                   "nonSpaceStringSegment", "optionValue", "nonSquareBracketString", 
                   "nonSpaceString", "singleTickEnclosedString", "doubleTickEnclosedString", 
                   "tickEnclosedString", "enclosedString", "cdromURI", "uriSchema", 
                   "commenterR", "wordWithPlus", "restSchemaWords", "genericURI", 
                   "uriR" ]

    EOF = Token.EOF
    TypeR=1
    OptionName=2
    CdromSchema=3
    Word=4
    WSS=5
    WS=6
    PunctuationAllowedInOptionValue=7
    OptionsStart=8
    OptionsEnd=9
    OptionNameValueSeparator=10
    CommentMarker=11
    Plus=12
    Colon=13
    OptionsSeparator=14
    Dash=15
    SingleTick=16
    DoubleTick=17
    WordChar=18
    NonWhitespaceNonOptionValueNonSquareRightBracketNonEq=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.2-SNAPSHOT")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.commented = None # CommenterR_opt_ourContext
            self.rType = None # Token
            self.options = None # OptionsR_opt_ourContext
            self.uri = None # UriRContext
            self.distribution = None # WordWithDashContext
            self.components = None # ComponentsRContext

        def WSS(self, i:int=None):
            if i is None:
                return self.getTokens(apt_sourceParser.WSS)
            else:
                return self.getToken(apt_sourceParser.WSS, i)

        def commenterR_opt_our(self):
            return self.getTypedRuleContext(apt_sourceParser.CommenterR_opt_ourContext,0)


        def TypeR(self):
            return self.getToken(apt_sourceParser.TypeR, 0)

        def optionsR_opt_our(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionsR_opt_ourContext,0)


        def uriR(self):
            return self.getTypedRuleContext(apt_sourceParser.UriRContext,0)


        def wordWithDash(self):
            return self.getTypedRuleContext(apt_sourceParser.WordWithDashContext,0)


        def componentsR(self):
            return self.getTypedRuleContext(apt_sourceParser.ComponentsRContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_record

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord" ):
                listener.enterRecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord" ):
                listener.exitRecord(self)




    def record(self):

        localctx = apt_sourceParser.RecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            localctx.commented = self.commenterR_opt_our()
            self.state = 59
            localctx.rType = self.match(apt_sourceParser.TypeR)
            self.state = 60
            self.match(apt_sourceParser.WSS)
            self.state = 61
            localctx.options = self.optionsR_opt_our()
            self.state = 62
            localctx.uri = self.uriR()
            self.state = 63
            self.match(apt_sourceParser.WSS)
            self.state = 64
            localctx.distribution = self.wordWithDash()
            self.state = 65
            localctx.components = self.componentsR()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 66
                self.match(apt_sourceParser.WSS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommenterR_opt_ourContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commenterR(self):
            return self.getTypedRuleContext(apt_sourceParser.CommenterRContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_commenterR_opt_our

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommenterR_opt_our" ):
                listener.enterCommenterR_opt_our(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommenterR_opt_our" ):
                listener.exitCommenterR_opt_our(self)




    def commenterR_opt_our(self):

        localctx = apt_sourceParser.CommenterR_opt_ourContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commenterR_opt_our)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 69
                self.commenterR()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionsR_opt_ourContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionsR(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionsRContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_optionsR_opt_our

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionsR_opt_our" ):
                listener.enterOptionsR_opt_our(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionsR_opt_our" ):
                listener.exitOptionsR_opt_our(self)




    def optionsR_opt_our(self):

        localctx = apt_sourceParser.OptionsR_opt_ourContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_optionsR_opt_our)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 72
                self.optionsR()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cId = None # WordWithDashContext

        def WSS(self):
            return self.getToken(apt_sourceParser.WSS, 0)

        def wordWithDash(self):
            return self.getTypedRuleContext(apt_sourceParser.WordWithDashContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_component

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent" ):
                listener.enterComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent" ):
                listener.exitComponent(self)




    def component(self):

        localctx = apt_sourceParser.ComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_component)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(apt_sourceParser.WSS)
            self.state = 76
            localctx.cId = self.wordWithDash()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentsRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.ComponentContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.ComponentContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_componentsR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponentsR" ):
                listener.enterComponentsR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponentsR" ):
                listener.exitComponentsR(self)




    def componentsR(self):

        localctx = apt_sourceParser.ComponentsRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_componentsR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 78
                    self.component()

                else:
                    raise NoViableAltException(self)
                self.state = 81 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionsRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pairs = None # OptionsListContext

        def OptionsStart(self):
            return self.getToken(apt_sourceParser.OptionsStart, 0)

        def OptionsEnd(self):
            return self.getToken(apt_sourceParser.OptionsEnd, 0)

        def WSS(self):
            return self.getToken(apt_sourceParser.WSS, 0)

        def optionsList(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionsListContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_optionsR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionsR" ):
                listener.enterOptionsR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionsR" ):
                listener.exitOptionsR(self)




    def optionsR(self):

        localctx = apt_sourceParser.OptionsRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_optionsR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(apt_sourceParser.OptionsStart)
            self.state = 84
            localctx.pairs = self.optionsList()
            self.state = 85
            self.match(apt_sourceParser.OptionsEnd)
            self.state = 86
            self.match(apt_sourceParser.WSS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionsListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.firstOption = None # OptionRContext
            self.restOptions = None # AdditionalOptionsContext

        def optionR(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionRContext,0)


        def additionalOptions(self):
            return self.getTypedRuleContext(apt_sourceParser.AdditionalOptionsContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_optionsList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionsList" ):
                listener.enterOptionsList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionsList" ):
                listener.exitOptionsList(self)




    def optionsList(self):

        localctx = apt_sourceParser.OptionsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_optionsList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            localctx.firstOption = self.optionR()
            self.state = 89
            localctx.restOptions = self.additionalOptions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionalOptionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additionalOption(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.AdditionalOptionContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.AdditionalOptionContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_additionalOptions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionalOptions" ):
                listener.enterAdditionalOptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionalOptions" ):
                listener.exitAdditionalOptions(self)




    def additionalOptions(self):

        localctx = apt_sourceParser.AdditionalOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additionalOptions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 91
                self.additionalOption()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionalOptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.separator = None # Token
            self.option = None # OptionRContext

        def OptionsSeparator(self):
            return self.getToken(apt_sourceParser.OptionsSeparator, 0)

        def optionR(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionRContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_additionalOption

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionalOption" ):
                listener.enterAdditionalOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionalOption" ):
                listener.exitAdditionalOption(self)




    def additionalOption(self):

        localctx = apt_sourceParser.AdditionalOptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_additionalOption)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            localctx.separator = self.match(apt_sourceParser.OptionsSeparator)
            self.state = 98
            localctx.option = self.optionR()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # Token
            self.value = None # OptionValueContext

        def OptionNameValueSeparator(self):
            return self.getToken(apt_sourceParser.OptionNameValueSeparator, 0)

        def OptionName(self):
            return self.getToken(apt_sourceParser.OptionName, 0)

        def optionValue(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionValueContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_optionR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionR" ):
                listener.enterOptionR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionR" ):
                listener.exitOptionR(self)




    def optionR(self):

        localctx = apt_sourceParser.OptionRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_optionR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            localctx.key = self.match(apt_sourceParser.OptionName)
            self.state = 101
            self.match(apt_sourceParser.OptionNameValueSeparator)
            self.state = 102
            localctx.value = self.optionValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordWithDashSegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(apt_sourceParser.Word, 0)

        def Dash(self):
            return self.getToken(apt_sourceParser.Dash, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_wordWithDashSegment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordWithDashSegment" ):
                listener.enterWordWithDashSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordWithDashSegment" ):
                listener.exitWordWithDashSegment(self)




    def wordWithDashSegment(self):

        localctx = apt_sourceParser.WordWithDashSegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_wordWithDashSegment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==4 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordWithDashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wordWithDashSegment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.WordWithDashSegmentContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.WordWithDashSegmentContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_wordWithDash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordWithDash" ):
                listener.enterWordWithDash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordWithDash" ):
                listener.exitWordWithDash(self)




    def wordWithDash(self):

        localctx = apt_sourceParser.WordWithDashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_wordWithDash)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.wordWithDashSegment()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionValueSegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self):
            return self.getToken(apt_sourceParser.Word, 0)

        def PunctuationAllowedInOptionValue(self):
            return self.getToken(apt_sourceParser.PunctuationAllowedInOptionValue, 0)

        def Dash(self):
            return self.getToken(apt_sourceParser.Dash, 0)

        def OptionName(self):
            return self.getToken(apt_sourceParser.OptionName, 0)

        def CdromSchema(self):
            return self.getToken(apt_sourceParser.CdromSchema, 0)

        def TypeR(self):
            return self.getToken(apt_sourceParser.TypeR, 0)

        def Plus(self):
            return self.getToken(apt_sourceParser.Plus, 0)

        def Colon(self):
            return self.getToken(apt_sourceParser.Colon, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_optionValueSegment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionValueSegment" ):
                listener.enterOptionValueSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionValueSegment" ):
                listener.exitOptionValueSegment(self)




    def optionValueSegment(self):

        localctx = apt_sourceParser.OptionValueSegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_optionValueSegment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 45214) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonSquareBracketStringSegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NonWhitespaceNonOptionValueNonSquareRightBracketNonEq(self):
            return self.getToken(apt_sourceParser.NonWhitespaceNonOptionValueNonSquareRightBracketNonEq, 0)

        def optionValueSegment(self):
            return self.getTypedRuleContext(apt_sourceParser.OptionValueSegmentContext,0)


        def OptionNameValueSeparator(self):
            return self.getToken(apt_sourceParser.OptionNameValueSeparator, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_nonSquareBracketStringSegment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonSquareBracketStringSegment" ):
                listener.enterNonSquareBracketStringSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonSquareBracketStringSegment" ):
                listener.exitNonSquareBracketStringSegment(self)




    def nonSquareBracketStringSegment(self):

        localctx = apt_sourceParser.NonSquareBracketStringSegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_nonSquareBracketStringSegment)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(apt_sourceParser.NonWhitespaceNonOptionValueNonSquareRightBracketNonEq)
                pass
            elif token in [1, 2, 3, 4, 7, 12, 13, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.optionValueSegment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(apt_sourceParser.OptionNameValueSeparator)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonSpaceStringSegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonSquareBracketStringSegment(self):
            return self.getTypedRuleContext(apt_sourceParser.NonSquareBracketStringSegmentContext,0)


        def OptionsEnd(self):
            return self.getToken(apt_sourceParser.OptionsEnd, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_nonSpaceStringSegment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonSpaceStringSegment" ):
                listener.enterNonSpaceStringSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonSpaceStringSegment" ):
                listener.exitNonSpaceStringSegment(self)




    def nonSpaceStringSegment(self):

        localctx = apt_sourceParser.NonSpaceStringSegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nonSpaceStringSegment)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 7, 10, 12, 13, 15, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.nonSquareBracketStringSegment()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(apt_sourceParser.OptionsEnd)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionValueSegment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.OptionValueSegmentContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.OptionValueSegmentContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_optionValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionValue" ):
                listener.enterOptionValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionValue" ):
                listener.exitOptionValue(self)




    def optionValue(self):

        localctx = apt_sourceParser.OptionValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_optionValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.optionValueSegment()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 45214) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonSquareBracketStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonSquareBracketStringSegment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.NonSquareBracketStringSegmentContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.NonSquareBracketStringSegmentContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_nonSquareBracketString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonSquareBracketString" ):
                listener.enterNonSquareBracketString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonSquareBracketString" ):
                listener.exitNonSquareBracketString(self)




    def nonSquareBracketString(self):

        localctx = apt_sourceParser.NonSquareBracketStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nonSquareBracketString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.nonSquareBracketStringSegment()
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 570526) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonSpaceStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonSpaceStringSegment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.NonSpaceStringSegmentContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.NonSpaceStringSegmentContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_nonSpaceString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonSpaceString" ):
                listener.enterNonSpaceString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonSpaceString" ):
                listener.exitNonSpaceString(self)




    def nonSpaceString(self):

        localctx = apt_sourceParser.NonSpaceStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_nonSpaceString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.nonSpaceStringSegment()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 571038) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleTickEnclosedStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SingleTick(self, i:int=None):
            if i is None:
                return self.getTokens(apt_sourceParser.SingleTick)
            else:
                return self.getToken(apt_sourceParser.SingleTick, i)

        def nonSquareBracketString(self):
            return self.getTypedRuleContext(apt_sourceParser.NonSquareBracketStringContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_singleTickEnclosedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTickEnclosedString" ):
                listener.enterSingleTickEnclosedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTickEnclosedString" ):
                listener.exitSingleTickEnclosedString(self)




    def singleTickEnclosedString(self):

        localctx = apt_sourceParser.SingleTickEnclosedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_singleTickEnclosedString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(apt_sourceParser.SingleTick)
            self.state = 138
            self.nonSquareBracketString()
            self.state = 139
            self.match(apt_sourceParser.SingleTick)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleTickEnclosedStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleTick(self, i:int=None):
            if i is None:
                return self.getTokens(apt_sourceParser.DoubleTick)
            else:
                return self.getToken(apt_sourceParser.DoubleTick, i)

        def nonSquareBracketString(self):
            return self.getTypedRuleContext(apt_sourceParser.NonSquareBracketStringContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_doubleTickEnclosedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleTickEnclosedString" ):
                listener.enterDoubleTickEnclosedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleTickEnclosedString" ):
                listener.exitDoubleTickEnclosedString(self)




    def doubleTickEnclosedString(self):

        localctx = apt_sourceParser.DoubleTickEnclosedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_doubleTickEnclosedString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(apt_sourceParser.DoubleTick)
            self.state = 142
            self.nonSquareBracketString()
            self.state = 143
            self.match(apt_sourceParser.DoubleTick)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TickEnclosedStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleTickEnclosedString(self):
            return self.getTypedRuleContext(apt_sourceParser.SingleTickEnclosedStringContext,0)


        def doubleTickEnclosedString(self):
            return self.getTypedRuleContext(apt_sourceParser.DoubleTickEnclosedStringContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_tickEnclosedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTickEnclosedString" ):
                listener.enterTickEnclosedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTickEnclosedString" ):
                listener.exitTickEnclosedString(self)




    def tickEnclosedString(self):

        localctx = apt_sourceParser.TickEnclosedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tickEnclosedString)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.singleTickEnclosedString()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.doubleTickEnclosedString()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnclosedStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OptionsStart(self):
            return self.getToken(apt_sourceParser.OptionsStart, 0)

        def tickEnclosedString(self):
            return self.getTypedRuleContext(apt_sourceParser.TickEnclosedStringContext,0)


        def OptionsEnd(self):
            return self.getToken(apt_sourceParser.OptionsEnd, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_enclosedString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnclosedString" ):
                listener.enterEnclosedString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnclosedString" ):
                listener.exitEnclosedString(self)




    def enclosedString(self):

        localctx = apt_sourceParser.EnclosedStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_enclosedString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(apt_sourceParser.OptionsStart)
            self.state = 150
            self.tickEnclosedString()
            self.state = 151
            self.match(apt_sourceParser.OptionsEnd)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CdromURIContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CdromSchema(self):
            return self.getToken(apt_sourceParser.CdromSchema, 0)

        def Colon(self):
            return self.getToken(apt_sourceParser.Colon, 0)

        def enclosedString(self):
            return self.getTypedRuleContext(apt_sourceParser.EnclosedStringContext,0)


        def nonSpaceString(self):
            return self.getTypedRuleContext(apt_sourceParser.NonSpaceStringContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_cdromURI

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCdromURI" ):
                listener.enterCdromURI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCdromURI" ):
                listener.exitCdromURI(self)




    def cdromURI(self):

        localctx = apt_sourceParser.CdromURIContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_cdromURI)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(apt_sourceParser.CdromSchema)
            self.state = 154
            self.match(apt_sourceParser.Colon)
            self.state = 155
            self.enclosedString()
            self.state = 156
            self.nonSpaceString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UriSchemaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.word = None # Token
            self.restWords = None # RestSchemaWordsContext

        def Word(self):
            return self.getToken(apt_sourceParser.Word, 0)

        def restSchemaWords(self):
            return self.getTypedRuleContext(apt_sourceParser.RestSchemaWordsContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_uriSchema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUriSchema" ):
                listener.enterUriSchema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUriSchema" ):
                listener.exitUriSchema(self)




    def uriSchema(self):

        localctx = apt_sourceParser.UriSchemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_uriSchema)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            localctx.word = self.match(apt_sourceParser.Word)
            self.state = 159
            localctx.restWords = self.restSchemaWords()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommenterRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CommentMarker(self):
            return self.getToken(apt_sourceParser.CommentMarker, 0)

        def WSS(self):
            return self.getToken(apt_sourceParser.WSS, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_commenterR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommenterR" ):
                listener.enterCommenterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommenterR" ):
                listener.exitCommenterR(self)




    def commenterR(self):

        localctx = apt_sourceParser.CommenterRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_commenterR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(apt_sourceParser.CommentMarker)
            self.state = 162
            self.match(apt_sourceParser.WSS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordWithPlusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.word = None # Token

        def Plus(self):
            return self.getToken(apt_sourceParser.Plus, 0)

        def Word(self):
            return self.getToken(apt_sourceParser.Word, 0)

        def getRuleIndex(self):
            return apt_sourceParser.RULE_wordWithPlus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWordWithPlus" ):
                listener.enterWordWithPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWordWithPlus" ):
                listener.exitWordWithPlus(self)




    def wordWithPlus(self):

        localctx = apt_sourceParser.WordWithPlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_wordWithPlus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(apt_sourceParser.Plus)
            self.state = 165
            localctx.word = self.match(apt_sourceParser.Word)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestSchemaWordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wordWithPlus(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(apt_sourceParser.WordWithPlusContext)
            else:
                return self.getTypedRuleContext(apt_sourceParser.WordWithPlusContext,i)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_restSchemaWords

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestSchemaWords" ):
                listener.enterRestSchemaWords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestSchemaWords" ):
                listener.exitRestSchemaWords(self)




    def restSchemaWords(self):

        localctx = apt_sourceParser.RestSchemaWordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_restSchemaWords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 167
                self.wordWithPlus()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericURIContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.schema = None # UriSchemaContext
            self.restOfURI = None # NonSpaceStringContext

        def Colon(self):
            return self.getToken(apt_sourceParser.Colon, 0)

        def uriSchema(self):
            return self.getTypedRuleContext(apt_sourceParser.UriSchemaContext,0)


        def nonSpaceString(self):
            return self.getTypedRuleContext(apt_sourceParser.NonSpaceStringContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_genericURI

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenericURI" ):
                listener.enterGenericURI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenericURI" ):
                listener.exitGenericURI(self)




    def genericURI(self):

        localctx = apt_sourceParser.GenericURIContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_genericURI)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            localctx.schema = self.uriSchema()
            self.state = 174
            self.match(apt_sourceParser.Colon)
            self.state = 175
            localctx.restOfURI = self.nonSpaceString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UriRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cdrom = None # CdromURIContext
            self.generic = None # GenericURIContext

        def cdromURI(self):
            return self.getTypedRuleContext(apt_sourceParser.CdromURIContext,0)


        def genericURI(self):
            return self.getTypedRuleContext(apt_sourceParser.GenericURIContext,0)


        def getRuleIndex(self):
            return apt_sourceParser.RULE_uriR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUriR" ):
                listener.enterUriR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUriR" ):
                listener.exitUriR(self)




    def uriR(self):

        localctx = apt_sourceParser.UriRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_uriR)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                localctx.cdrom = self.cdromURI()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                localctx.generic = self.genericURI()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





