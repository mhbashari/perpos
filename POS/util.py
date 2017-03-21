from nltk import tree2conlltags


def read_conll(path, col=2):
    with open(path, "r", encoding="utf-8") as conll:
        out = []
        for sent in conll.readlines():
            split = sent.strip("\r\n").split()
            if len(split) > 1:
                none_token_count = col - 1
                new_elem = split[-1:]
                new_elem = split[:none_token_count] + new_elem
                out.append(new_elem)

            else:
                yield out
                out = []


def template(word):
    return "".join([(lambda item: "x" if not item in "آایو" else "a")(char) for char in word])


def isdigit(word):
    return all(map(lambda char: char in "۱۲۳۴۵۶۷۸۹۰1234567890.", word))


def ngram(word, leng=2):
    for i in range(len(word) - 1):
        yield 'word[' + str(i) + ":" + str(i + leng) + "]", word[i:i + leng]


def tree2brackets(tree):
    str, tag = '', ''
    for item in tree2conlltags(tree):
        if item[2][0] in {'B', 'O'} and tag:
            str += tag + '] '
            tag = ''

        if item[2][0] == 'B':
            tag = item[2].split('-')[1]
            str += '['
        str += item[0] + ' '

    if tag:
        str += tag + '] '

    return str.strip()
