# Generated from grammar.g4 by ANTLR 4.11.2-SNAPSHOT
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .apt_sourceParser import apt_sourceParser
else:
    from apt_sourceParser import apt_sourceParser

# This class defines a complete listener for a parse tree produced by apt_sourceParser.
class apt_sourceListener(ParseTreeListener):

    # Enter a parse tree produced by apt_sourceParser#record.
    def enterRecord(self, ctx:apt_sourceParser.RecordContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#record.
    def exitRecord(self, ctx:apt_sourceParser.RecordContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#commenterR_opt_our.
    def enterCommenterR_opt_our(self, ctx:apt_sourceParser.CommenterR_opt_ourContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#commenterR_opt_our.
    def exitCommenterR_opt_our(self, ctx:apt_sourceParser.CommenterR_opt_ourContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#optionsR_opt_our.
    def enterOptionsR_opt_our(self, ctx:apt_sourceParser.OptionsR_opt_ourContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#optionsR_opt_our.
    def exitOptionsR_opt_our(self, ctx:apt_sourceParser.OptionsR_opt_ourContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#component.
    def enterComponent(self, ctx:apt_sourceParser.ComponentContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#component.
    def exitComponent(self, ctx:apt_sourceParser.ComponentContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#componentsR.
    def enterComponentsR(self, ctx:apt_sourceParser.ComponentsRContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#componentsR.
    def exitComponentsR(self, ctx:apt_sourceParser.ComponentsRContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#optionsR.
    def enterOptionsR(self, ctx:apt_sourceParser.OptionsRContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#optionsR.
    def exitOptionsR(self, ctx:apt_sourceParser.OptionsRContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#optionsList.
    def enterOptionsList(self, ctx:apt_sourceParser.OptionsListContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#optionsList.
    def exitOptionsList(self, ctx:apt_sourceParser.OptionsListContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#additionalOptions.
    def enterAdditionalOptions(self, ctx:apt_sourceParser.AdditionalOptionsContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#additionalOptions.
    def exitAdditionalOptions(self, ctx:apt_sourceParser.AdditionalOptionsContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#additionalOption.
    def enterAdditionalOption(self, ctx:apt_sourceParser.AdditionalOptionContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#additionalOption.
    def exitAdditionalOption(self, ctx:apt_sourceParser.AdditionalOptionContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#optionR.
    def enterOptionR(self, ctx:apt_sourceParser.OptionRContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#optionR.
    def exitOptionR(self, ctx:apt_sourceParser.OptionRContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#wordWithDashSegment.
    def enterWordWithDashSegment(self, ctx:apt_sourceParser.WordWithDashSegmentContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#wordWithDashSegment.
    def exitWordWithDashSegment(self, ctx:apt_sourceParser.WordWithDashSegmentContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#wordWithDash.
    def enterWordWithDash(self, ctx:apt_sourceParser.WordWithDashContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#wordWithDash.
    def exitWordWithDash(self, ctx:apt_sourceParser.WordWithDashContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#optionValueSegment.
    def enterOptionValueSegment(self, ctx:apt_sourceParser.OptionValueSegmentContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#optionValueSegment.
    def exitOptionValueSegment(self, ctx:apt_sourceParser.OptionValueSegmentContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#nonSquareBracketStringSegment.
    def enterNonSquareBracketStringSegment(self, ctx:apt_sourceParser.NonSquareBracketStringSegmentContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#nonSquareBracketStringSegment.
    def exitNonSquareBracketStringSegment(self, ctx:apt_sourceParser.NonSquareBracketStringSegmentContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#nonSpaceStringSegment.
    def enterNonSpaceStringSegment(self, ctx:apt_sourceParser.NonSpaceStringSegmentContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#nonSpaceStringSegment.
    def exitNonSpaceStringSegment(self, ctx:apt_sourceParser.NonSpaceStringSegmentContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#optionValue.
    def enterOptionValue(self, ctx:apt_sourceParser.OptionValueContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#optionValue.
    def exitOptionValue(self, ctx:apt_sourceParser.OptionValueContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#nonSquareBracketString.
    def enterNonSquareBracketString(self, ctx:apt_sourceParser.NonSquareBracketStringContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#nonSquareBracketString.
    def exitNonSquareBracketString(self, ctx:apt_sourceParser.NonSquareBracketStringContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#nonSpaceString.
    def enterNonSpaceString(self, ctx:apt_sourceParser.NonSpaceStringContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#nonSpaceString.
    def exitNonSpaceString(self, ctx:apt_sourceParser.NonSpaceStringContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#singleTickEnclosedString.
    def enterSingleTickEnclosedString(self, ctx:apt_sourceParser.SingleTickEnclosedStringContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#singleTickEnclosedString.
    def exitSingleTickEnclosedString(self, ctx:apt_sourceParser.SingleTickEnclosedStringContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#doubleTickEnclosedString.
    def enterDoubleTickEnclosedString(self, ctx:apt_sourceParser.DoubleTickEnclosedStringContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#doubleTickEnclosedString.
    def exitDoubleTickEnclosedString(self, ctx:apt_sourceParser.DoubleTickEnclosedStringContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#tickEnclosedString.
    def enterTickEnclosedString(self, ctx:apt_sourceParser.TickEnclosedStringContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#tickEnclosedString.
    def exitTickEnclosedString(self, ctx:apt_sourceParser.TickEnclosedStringContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#enclosedString.
    def enterEnclosedString(self, ctx:apt_sourceParser.EnclosedStringContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#enclosedString.
    def exitEnclosedString(self, ctx:apt_sourceParser.EnclosedStringContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#cdromURI.
    def enterCdromURI(self, ctx:apt_sourceParser.CdromURIContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#cdromURI.
    def exitCdromURI(self, ctx:apt_sourceParser.CdromURIContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#uriSchema.
    def enterUriSchema(self, ctx:apt_sourceParser.UriSchemaContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#uriSchema.
    def exitUriSchema(self, ctx:apt_sourceParser.UriSchemaContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#commenterR.
    def enterCommenterR(self, ctx:apt_sourceParser.CommenterRContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#commenterR.
    def exitCommenterR(self, ctx:apt_sourceParser.CommenterRContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#wordWithPlus.
    def enterWordWithPlus(self, ctx:apt_sourceParser.WordWithPlusContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#wordWithPlus.
    def exitWordWithPlus(self, ctx:apt_sourceParser.WordWithPlusContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#restSchemaWords.
    def enterRestSchemaWords(self, ctx:apt_sourceParser.RestSchemaWordsContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#restSchemaWords.
    def exitRestSchemaWords(self, ctx:apt_sourceParser.RestSchemaWordsContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#genericURI.
    def enterGenericURI(self, ctx:apt_sourceParser.GenericURIContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#genericURI.
    def exitGenericURI(self, ctx:apt_sourceParser.GenericURIContext):
        pass


    # Enter a parse tree produced by apt_sourceParser#uriR.
    def enterUriR(self, ctx:apt_sourceParser.UriRContext):
        pass

    # Exit a parse tree produced by apt_sourceParser#uriR.
    def exitUriR(self, ctx:apt_sourceParser.UriRContext):
        pass



del apt_sourceParser