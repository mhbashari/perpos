import string

from POS.util import template, isdigit, ngram


def word2features(sent, i):
    W = sent[i]
    features = {
        'B': 1.0,
        'W': W,
        'P': W in string.punctuation,
        'T': template(W),
        'D(W)': isdigit(W),
    }
    for leng in range(max(4 + 1, len(W)) + 1):
        for k, v in ngram(W, leng=leng):
            features[k] = v
    if i > 0:
        W = sent[i - 1][0]
        features.update({
            '-1W[-3': W[-3:],
            '-1W[-2': W[-2:],
            '-1W[-1': W[-1:],
            '-1W': W,
            '-1W0W': W + sent[i],
            '-1P': W in string.punctuation,
            '-1T': template(W)
        })
    else:
        features['BOS'] = True
    if i > 1:
        W = sent[i - 2][0]
        features.update({
            '-2W[-3': W[-3:],
            '-2W[-2': W[-2:],
            '-2W[-1': W[-1:],
            '-2P': W in string.punctuation,
            '-2T': template(W)
        })

    if i < len(sent) - 2:
        W = sent[i + 2][0]
        features.update({
            '+2W[-1': W[-1:],
            '+2W[-2': W[-2:],
            '+2W': W,
            '+2P': W in string.punctuation,
            '+2T': template(W)
        })
    if i < len(sent) - 1:
        W = sent[i + 1][0]
        features.update({
            '+1W[-1': W[-1:],
            '+1W': W,
            '+1W0W': W + sent[i],
            '+1W[-2': W[-2:],
            '+1:P': W in string.punctuation,
            '+1:T': template(W)
        })
    else:
        features['EOS'] = True
    if 0 < i < len(sent) - 1:
        features['-1W/+1W'] = sent[i + 1][0] + "/" + sent[i - 1][0]
    return features


def token2features(token_list):
    return [word2features(token_list, i) for i in range(len(token_list))]


def sent2labels(sent):
    return [postag for token, postag in sent]


def sent2tokens(sent):
    return [token for token, postag in sent]
