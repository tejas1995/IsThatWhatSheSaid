import nltk
import collections

START_SYMBOL = "*"
STOP_SYMBOL = 'STOP'


def buildWordset(train_sents):

    wordset = set([])

    for sent in train_sents:
        wordset.update(sent)

    return list(wordset)


def buildBigramSet(train_sents):

    bigramCount = collections.defaultdict(int)

    train_sents = [[START_SYMBOL] + sent + [STOP_SYMBOL] for sent in train_sents]

    for sent in train_sents:
        new_bigrams = nltk.bigrams(sent)
        for bg in new_bigrams:
            bigramCount[bg] += 1

    propBigrams = [bg for bg, count in bigramCount.iteritems() if count >= 2]
    return propBigrams


def extractUnigramFeatures(list_sents, wordset):

    sent_features = []

    for sent in list_sents:
        sent_features.append([sent.count(w) for w in wordset])

    return sent_features
