from lib import LexicalAnalyzer

TokenDefinitions = [
    ('Mod', '(%)'),
    ('Dot', '(\\.)'),
    ('Comma', '(,)'),
    ('Colon', '(:)'),
    ('Assign', '(=)'),
    ('Equal', '(==)'),
    ('Division', '(/)'),
    ('Operator', '(!=)'),
    ('Comment', '(#.*)'),
    ('Addition', '(\\+)'),
    ('Subtraction', '(-)'),
    ('Chevrons', '(\\<|\\>)'),
    ('Brackets', '(\\[|\\])'),
    ('Multiplication', '(\\*)'),
    ('Parentheses', '(\\(|\\))'),
    ('String', '(\"([^"]*?)\")'),
    ('String', '(\'([^\']*?)\')'),
    ('Number', '([-+]?\\d*.?\\d+)'),
]

ReservedWordsFile = open("ReservedWords.txt", "r")
for line in ReservedWordsFile:
    if (line.strip()):
        TokenDefinitions.append(("Keyword", '(%s)' % line.strip()))

TokenDefinitions.append(("Identifier", "([A-Za-z_]\w*)"))

SampleCode = open("sample.py", "r")

Tokens = LexicalAnalyzer.Analyze('\r\n'.join(SampleCode.readlines()),
                                 TokenDefinitions)

print('−' * (30 * 4 + 3 * 3 + 2))
print('|{:^30s} | {:^30s} | {:^30s} | {:^30s}|'.format('Index', 'Offset',
                                                       'Value', 'Type'))
print('|' + ('−' * (30 * 4 + 3 * 3)) + '|')
list(
    map(
        lambda x: print('|{:^30d} | {:^30d} | {:^30s} | {:^30s}|'.format(
            x.index, x.offset, x.value, x.type) + '\r\n' +
                        ('|' + ('−' * (30 * 4 + 3 * 3)) + '|')), Tokens))
