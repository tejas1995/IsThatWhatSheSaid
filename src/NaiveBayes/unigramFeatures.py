def buildWordset(train_sents):

    wordset = set([])

    for sent in train_sents:
        wordset.update(sent)

    return wordset


def extractFeatures(list_sents, wordset):

    sent_features = []

    for sent in list_sents:
        sent_features.append([sent.count(w) for w in wordset])

    return sent_features
