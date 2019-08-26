grammar apt;


WSC: [\p{White_Space}];
NWSC: ~[\p{White_Space}];

WS: [\p{White_Space}]+;
NonSpaceString: NWSC+;

OptionsStart: '[';
OptionsEnd: ']';
Word: [a-zA-Z_]+;
OptionValue: [a-zA-Z0-9_/.-]+;
OptionNameValueSeparator: '=';

CommentMarker: '#';

Cdrom: 'cdrom';
CdromSchema: Cdrom ':';

NonSquareBracketString: ~[\]]+;

Distribution: [a-zA-Z_-]+;
ComponentName: [a-zA-Z_-]+;

/////////////////
genericURI: (Word '+')* Word ':' NonSpaceString;
enclosedString: OptionsStart ('\'' NonSquareBracketString '\'' | '"' NonSquareBracketString '"') OptionsEnd;
cdromURI: CdromSchema enclosedString NonSpaceString;


record: commenter? type WS options? uri WS Distribution component+ WS*;
component: WS ComponentName;

type: 'deb' | 'deb-src';

options: OptionsStart optionsList OptionsEnd WS;
optionsList: option additionalOption*;
additionalOption: optionsSeparator option;
option: optionName OptionNameValueSeparator OptionValue;
optionName: 'arch' | 'lang' | 'target' | 'pdiffs' | 'by-hash' | 'valid-until-max' | 'allow-downgrade-to-insecure' | 'allow-weak' | 'allow-insecure' | 'trusted' | 'signed-by' | 'check-valid-until' | 'valid-until-min' | 'check-date' | 'inrelease-path' | 'date-max-future';

optionsSeparator: ',';

uri: cdromURI | genericURI;

commenter: CommentMarker ?WS;

