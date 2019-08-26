#!/usr/bin/env python

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import annotations

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.parsing import leftrec, nomemo, isname # noqa
from tatsu.infos import ParserConfig
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class apt_sourceBuffer(Buffer):
    def __init__(self, text, /, config: ParserConfig = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace=None,
            nameguard=None,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=False,
            namechars='',
            parseinfo=False,
        )
        config = config.replace(**settings)
        super().__init__(text, config=config)


class apt_sourceParser(Parser):
    def __init__(self, /, config: ParserConfig = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace=None,
            nameguard=None,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=False,
            namechars='',
            parseinfo=False,
            keywords=KEYWORDS,
        )
        config = config.replace(**settings)
        super().__init__(config=config)

    @tatsumasu()
    def _record_(self):  # noqa
        self._commenterR_opt_our_()
        self.name_last_node('commented')
        self._TypeR_()
        self.name_last_node('rType')
        self._WSS_()
        self._optionsR_opt_our_()
        self.name_last_node('options')
        self._uriR_()
        self.name_last_node('uri')
        self._WSS_()
        self._wordWithDash_()
        self.name_last_node('distribution')
        self._componentsR_()
        self.name_last_node('components')
        with self._optional():
            self._WSS_()
        self._define(
            ['commented', 'components', 'distribution', 'options', 'rType', 'uri'],
            []
        )

    @tatsumasu()
    def _commenterR_opt_our_(self):  # noqa
        with self._optional():
            self._commenterR_()

    @tatsumasu()
    def _optionsR_opt_our_(self):  # noqa
        with self._optional():
            self._optionsR_()

    @tatsumasu()
    def _component_(self):  # noqa
        self._WSS_()
        self._wordWithDash_()
        self.name_last_node('cId')
        self._define(
            ['cId'],
            []
        )

    @tatsumasu()
    def _componentsR_(self):  # noqa

        def block0():
            self._component_()
        self._positive_closure(block0)

    @tatsumasu()
    def _optionsR_(self):  # noqa
        self._OptionsStart_()
        self._optionsList_()
        self.name_last_node('pairs')
        self._OptionsEnd_()
        self._WSS_()
        self._define(
            ['pairs'],
            []
        )

    @tatsumasu()
    def _optionsList_(self):  # noqa
        self._optionR_()
        self.name_last_node('firstOption')
        self._additionalOptions_()
        self.name_last_node('restOptions')
        self._define(
            ['firstOption', 'restOptions'],
            []
        )

    @tatsumasu()
    def _additionalOptions_(self):  # noqa

        def block0():
            self._additionalOption_()
        self._closure(block0)

    @tatsumasu()
    def _additionalOption_(self):  # noqa
        self._OptionsSeparator_()
        self.name_last_node('separator')
        self._optionR_()
        self.name_last_node('option')
        self._define(
            ['option', 'separator'],
            []
        )

    @tatsumasu()
    def _optionR_(self):  # noqa
        self._OptionName_()
        self.name_last_node('key')
        self._OptionNameValueSeparator_()
        self._optionValue_()
        self.name_last_node('value')
        self._define(
            ['key', 'value'],
            []
        )

    @tatsumasu()
    def _wordWithDashSegment_(self):  # noqa
        with self._choice():
            with self._option():
                self._Word_()
            with self._option():
                self._Dash_()
            self._error(
                'expecting one of: '
                "'-' <Dash> <Word> <WordChar>"
                '[0-9A-Z_a-z]'
            )

    @tatsumasu()
    def _wordWithDash_(self):  # noqa

        def block0():
            self._wordWithDashSegment_()
        self._positive_closure(block0)

    @tatsumasu()
    def _optionValueSegment_(self):  # noqa
        with self._choice():
            with self._option():
                self._Word_()
            with self._option():
                self._PunctuationAllowedInOptionValue_()
            with self._option():
                self._Dash_()
            with self._option():
                self._OptionName_()
            with self._option():
                self._CdromSchema_()
            with self._option():
                self._TypeR_()
            with self._option():
                self._Plus_()
            with self._option():
                self._Colon_()
            self._error(
                'expecting one of: '
                "'+' '-' ':' 'allow-downgrade-to-"
                "insecure' 'allow-insecure' 'allow-weak'"
                "'arch' 'by-hash' 'cdrom:' 'check-date'"
                "'check-valid-until' 'date-max-future'"
                "'deb' 'deb-src' 'inrelease-path' 'lang'"
                "'pdiffs' 'signed-by' 'target' 'trusted'"
                "'valid-until-max' 'valid-until-min'"
                '<CdromSchema> <Colon> <Dash>'
                '<OptionName> <Plus>'
                '<PunctuationAllowedInOptionValue>'
                '<TypeR> <Word> <WordChar> [0-9A-Z_a-z]'
                '[\\/\\.]'
            )

    @tatsumasu()
    def _nonSquareBracketStringSegment_(self):  # noqa
        with self._choice():
            with self._option():
                self._NonWhitespaceNonOptionValueNonSquareRightBracketNonEq_()
            with self._option():
                self._optionValueSegment_()
            with self._option():
                self._OptionNameValueSeparator_()
            self._error(
                'expecting one of: '
                "'+' '-' ':' '=' 'allow-downgrade-to-"
                "insecure' 'allow-insecure' 'allow-weak'"
                "'arch' 'by-hash' 'cdrom:' 'check-date'"
                "'check-valid-until' 'date-max-future'"
                "'deb' 'deb-src' 'inrelease-path' 'lang'"
                "'pdiffs' 'signed-by' 'target' 'trusted'"
                "'valid-until-max' 'valid-until-min'"
                '<CdromSchema> <Colon> <Dash> <NonWhitesp'
                'aceNonOptionValueNonSquareRightBracketNo'
                'nEq> <OptionName>'
                '<OptionNameValueSeparator> <Plus>'
                '<PunctuationAllowedInOptionValue>'
                '<TypeR> <Word> <WordChar>'
                '<optionValueSegment> [0-9A-Z_a-z] [\\/\\.]'
                '[^\\t-\\r\\ "\\#\'\\+-:=A-\\]_a-z]'
            )

    @tatsumasu()
    def _nonSpaceStringSegment_(self):  # noqa
        with self._choice():
            with self._option():
                self._nonSquareBracketStringSegment_()
            with self._option():
                self._OptionsEnd_()
            self._error(
                'expecting one of: '
                "'+' '-' ':' '=' ']' 'allow-downgrade-to-"
                "insecure' 'allow-insecure' 'allow-weak'"
                "'arch' 'by-hash' 'cdrom:' 'check-date'"
                "'check-valid-until' 'date-max-future'"
                "'deb' 'deb-src' 'inrelease-path' 'lang'"
                "'pdiffs' 'signed-by' 'target' 'trusted'"
                "'valid-until-max' 'valid-until-min'"
                '<CdromSchema> <Colon> <Dash> <NonWhitesp'
                'aceNonOptionValueNonSquareRightBracketNo'
                'nEq> <OptionName>'
                '<OptionNameValueSeparator> <OptionsEnd>'
                '<Plus> <PunctuationAllowedInOptionValue>'
                '<TypeR> <Word> <WordChar>'
                '<nonSquareBracketStringSegment>'
                '<optionValueSegment> [0-9A-Z_a-z] [\\/\\.]'
                '[^\\t-\\r\\ "\\#\'\\+-:=A-\\]_a-z]'
            )

    @tatsumasu()
    def _optionValue_(self):  # noqa

        def block0():
            self._optionValueSegment_()
        self._positive_closure(block0)

    @tatsumasu()
    def _nonSquareBracketString_(self):  # noqa

        def block0():
            self._nonSquareBracketStringSegment_()
        self._positive_closure(block0)

    @tatsumasu()
    def _nonSpaceString_(self):  # noqa

        def block0():
            self._nonSpaceStringSegment_()
        self._positive_closure(block0)

    @tatsumasu()
    def _singleTickEnclosedString_(self):  # noqa
        self._SingleTick_()
        self._nonSquareBracketString_()
        self._SingleTick_()

    @tatsumasu()
    def _doubleTickEnclosedString_(self):  # noqa
        self._DoubleTick_()
        self._nonSquareBracketString_()
        self._DoubleTick_()

    @tatsumasu()
    def _tickEnclosedString_(self):  # noqa
        with self._choice():
            with self._option():
                self._singleTickEnclosedString_()
            with self._option():
                self._doubleTickEnclosedString_()
            self._error(
                'expecting one of: '
                '"\'" \'"\' <DoubleTick> <SingleTick>'
                '<doubleTickEnclosedString>'
                '<singleTickEnclosedString>'
            )

    @tatsumasu()
    def _enclosedString_(self):  # noqa
        self._OptionsStart_()
        self._tickEnclosedString_()
        self._OptionsEnd_()

    @tatsumasu()
    def _cdromURI_(self):  # noqa
        self._CdromSchema_()
        self._Colon_()
        self._enclosedString_()
        self._nonSpaceString_()

    @tatsumasu()
    def _uriSchema_(self):  # noqa
        self._Word_()
        self.name_last_node('word')
        self._restSchemaWords_()
        self.name_last_node('restWords')
        self._define(
            ['restWords', 'word'],
            []
        )

    @tatsumasu()
    def _commenterR_(self):  # noqa
        self._CommentMarker_()
        self._WSS_()

    @tatsumasu()
    def _wordWithPlus_(self):  # noqa
        self._Plus_()
        self._Word_()
        self.name_last_node('word')
        self._define(
            ['word'],
            []
        )

    @tatsumasu()
    def _restSchemaWords_(self):  # noqa

        def block0():
            self._wordWithPlus_()
        self._closure(block0)

    @tatsumasu()
    def _genericURI_(self):  # noqa
        self._uriSchema_()
        self.name_last_node('schema')
        self._Colon_()
        self._nonSpaceString_()
        self.name_last_node('restOfURI')
        self._define(
            ['restOfURI', 'schema'],
            []
        )

    @tatsumasu()
    def _uriR_(self):  # noqa
        with self._choice():
            with self._option():
                self._cdromURI_()
                self.name_last_node('cdrom')
                self._define(
                    ['cdrom'],
                    []
                )
            with self._option():
                self._genericURI_()
                self.name_last_node('generic')
                self._define(
                    ['generic'],
                    []
                )
            self._error(
                'expecting one of: '
                "'cdrom:' <CdromSchema> <Word> <WordChar>"
                '<cdromURI> <genericURI> <uriSchema>'
                '[0-9A-Z_a-z]'
            )
        self._define(
            ['cdrom', 'generic'],
            []
        )

    @tatsumasu()
    def _TypeR_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('deb')
            with self._option():
                self._token('deb-src')
            self._error(
                'expecting one of: '
                "'deb' 'deb-src'"
            )

    @tatsumasu()
    def _OptionName_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('arch')
            with self._option():
                self._token('lang')
            with self._option():
                self._token('target')
            with self._option():
                self._token('pdiffs')
            with self._option():
                self._token('by-hash')
            with self._option():
                self._token('valid-until-max')
            with self._option():
                self._token('allow-downgrade-to-insecure')
            with self._option():
                self._token('allow-weak')
            with self._option():
                self._token('allow-insecure')
            with self._option():
                self._token('trusted')
            with self._option():
                self._token('signed-by')
            with self._option():
                self._token('check-valid-until')
            with self._option():
                self._token('valid-until-min')
            with self._option():
                self._token('check-date')
            with self._option():
                self._token('inrelease-path')
            with self._option():
                self._token('date-max-future')
            self._error(
                'expecting one of: '
                "'allow-downgrade-to-insecure' 'allow-"
                "insecure' 'allow-weak' 'arch' 'by-hash'"
                "'check-date' 'check-valid-until' 'date-"
                "max-future' 'inrelease-path' 'lang'"
                "'pdiffs' 'signed-by' 'target' 'trusted'"
                "'valid-until-max' 'valid-until-min'"
            )

    @tatsumasu()
    def _CdromSchema_(self):  # noqa
        self._token('cdrom:')

    @tatsumasu()
    def _WS_(self):  # noqa
        self._pattern('[\\t-\\r\\ ]')

    @tatsumasu()
    def _PunctuationAllowedInOptionValue_(self):  # noqa
        self._pattern('[\\/\\.]')

    @tatsumasu()
    def _OptionsStart_(self):  # noqa
        self._token('[')

    @tatsumasu()
    def _OptionsEnd_(self):  # noqa
        self._token(']')

    @tatsumasu()
    def _OptionNameValueSeparator_(self):  # noqa
        self._token('=')

    @tatsumasu()
    def _CommentMarker_(self):  # noqa
        self._token('#')

    @tatsumasu()
    def _Plus_(self):  # noqa
        self._token('+')

    @tatsumasu()
    def _Colon_(self):  # noqa
        self._token(':')

    @tatsumasu()
    def _OptionsSeparator_(self):  # noqa
        self._token(',')

    @tatsumasu()
    def _Dash_(self):  # noqa
        self._token('-')

    @tatsumasu()
    def _SingleTick_(self):  # noqa
        self._token("'")

    @tatsumasu()
    def _DoubleTick_(self):  # noqa
        self._token('"')

    @tatsumasu()
    def _WordChar_(self):  # noqa
        self._pattern('[0-9A-Z_a-z]')

    @tatsumasu()
    def _NonWhitespaceNonOptionValueNonSquareRightBracketNonEq_(self):  # noqa
        self._pattern('[^\\t-\\r\\ "\\#\'\\+-:=A-\\]_a-z]')

    @tatsumasu()
    def _Word_(self):  # noqa

        def block0():
            self._WordChar_()
        self._positive_closure(block0)

    @tatsumasu()
    def _WSS_(self):  # noqa

        def block0():
            self._WS_()
        self._positive_closure(block0)


class apt_sourceSemantics:
    def record(self, ast):  # noqa
        return ast

    def commenterR_opt_our(self, ast):  # noqa
        return ast

    def optionsR_opt_our(self, ast):  # noqa
        return ast

    def component(self, ast):  # noqa
        return ast

    def componentsR(self, ast):  # noqa
        return ast

    def optionsR(self, ast):  # noqa
        return ast

    def optionsList(self, ast):  # noqa
        return ast

    def additionalOptions(self, ast):  # noqa
        return ast

    def additionalOption(self, ast):  # noqa
        return ast

    def optionR(self, ast):  # noqa
        return ast

    def wordWithDashSegment(self, ast):  # noqa
        return ast

    def wordWithDash(self, ast):  # noqa
        return ast

    def optionValueSegment(self, ast):  # noqa
        return ast

    def nonSquareBracketStringSegment(self, ast):  # noqa
        return ast

    def nonSpaceStringSegment(self, ast):  # noqa
        return ast

    def optionValue(self, ast):  # noqa
        return ast

    def nonSquareBracketString(self, ast):  # noqa
        return ast

    def nonSpaceString(self, ast):  # noqa
        return ast

    def singleTickEnclosedString(self, ast):  # noqa
        return ast

    def doubleTickEnclosedString(self, ast):  # noqa
        return ast

    def tickEnclosedString(self, ast):  # noqa
        return ast

    def enclosedString(self, ast):  # noqa
        return ast

    def cdromURI(self, ast):  # noqa
        return ast

    def uriSchema(self, ast):  # noqa
        return ast

    def commenterR(self, ast):  # noqa
        return ast

    def wordWithPlus(self, ast):  # noqa
        return ast

    def restSchemaWords(self, ast):  # noqa
        return ast

    def genericURI(self, ast):  # noqa
        return ast

    def uriR(self, ast):  # noqa
        return ast

    def TypeR(self, ast):  # noqa
        return ast

    def OptionName(self, ast):  # noqa
        return ast

    def CdromSchema(self, ast):  # noqa
        return ast

    def WS(self, ast):  # noqa
        return ast

    def PunctuationAllowedInOptionValue(self, ast):  # noqa
        return ast

    def OptionsStart(self, ast):  # noqa
        return ast

    def OptionsEnd(self, ast):  # noqa
        return ast

    def OptionNameValueSeparator(self, ast):  # noqa
        return ast

    def CommentMarker(self, ast):  # noqa
        return ast

    def Plus(self, ast):  # noqa
        return ast

    def Colon(self, ast):  # noqa
        return ast

    def OptionsSeparator(self, ast):  # noqa
        return ast

    def Dash(self, ast):  # noqa
        return ast

    def SingleTick(self, ast):  # noqa
        return ast

    def DoubleTick(self, ast):  # noqa
        return ast

    def WordChar(self, ast):  # noqa
        return ast

    def NonWhitespaceNonOptionValueNonSquareRightBracketNonEq(self, ast):  # noqa
        return ast

    def Word(self, ast):  # noqa
        return ast

    def WSS(self, ast):  # noqa
        return ast


def main(filename, start=None, **kwargs):
    if start is None:
        start = 'record'
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = apt_sourceParser()
    return parser.parse(
        text,
        rule_name=start,
        filename=filename,
        **kwargs
    )


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, apt_sourceParser, name='apt_source')
    data = asjson(ast)
    print(json.dumps(data, indent=2))
