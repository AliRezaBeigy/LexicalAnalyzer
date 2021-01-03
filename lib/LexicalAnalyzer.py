import re


class Token:
    def __init__(self, index, offset, value, type):
        self.type = type
        self.value = value
        self.index = index
        self.offset = offset


def Analyze(inputString, tokenDefinitions):
    index = 0
    offset = 0
    tokens = []

    while len(inputString):
        isMatched = False
        for i in range(0, len(tokenDefinitions)):
            tokenDefinition = tokenDefinitions[i]
            match = re.search('^' + tokenDefinition[1], inputString)
            if match is not None:
                matched = match.group(1)
                length = len(matched)

                tokens.append(Token(index, offset, matched,
                                    tokenDefinition[0]))

                index += 1
                offset += length
                isMatched = True
                inputString = inputString[length:].strip()
                break
        if not isMatched:
            raise Exception('At %s\r\n %s' % (offset, inputString.split()[0]))
    return tokens