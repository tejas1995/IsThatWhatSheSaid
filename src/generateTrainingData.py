import nltk
import pickle

from nltk.corpus import brown
from nltk.tokenize.treebank import TreebankWordTokenizer as WT


def generateBrownPickle():

    '''
    Retrieve 120 sentences from each category in the Brown corpus.
    Pickle the data
    '''

    brown_sents = []
    for cat in brown.categories():
        for sent in brown.sents(categories=cat)[:120]:
            brown_sents.append(sent)

    # Convert all sentences to lowercase
    for sent in brown_sents:
        sent = [w.lower() for w in sent]

    brown_pickle = open('../data/brown_data.pk', 'wb')
    pickle.dump(brown_sents, brown_pickle)
    brown_pickle.close()

generateBrownPickle()


def generateTWSSPickle():

    '''
    Tokenize and pickle the TWSS sentences
    '''

    twss_file = open('../data/TWSS_sents.txt')
    twss_sents = twss_file.readlines()
    twss_tokenized_sents = []

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    for sent in twss_sents:
        twss_tokenized_sents.append(WT().tokenize(sent.strip()))

    # Convert all sentences to lowercase
    for sent in twss_tokenized_sents:
        sent = [w.lower() for w in sent]

    twss_pickle = open('../data/TWSS_data.pk', 'wb')
    pickle.dump(twss_tokenized_sents, twss_pickle)
    twss_pickle.close()

generateTWSSPickle()
