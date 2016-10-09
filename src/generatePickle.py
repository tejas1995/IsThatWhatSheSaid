import nltk
import pickle

from nltk.corpus import brown
from nltk.tokenize.treebank import TreebankWordTokenizer as TWT

from os import path


def generateBrownPickle():

    '''
    Retrieve 150 sentences from each category in the Brown corpus.
    Pickle the data
    '''

    brown_sents = []
    for cat in brown.categories():
        for sent in brown.sents(categories=cat)[:150]:
            brown_sents.append(sent)

    # Convert all sentences to lowercase
    for sent in brown_sents:
        sent = [w.lower() for w in sent]

    brown_file = path.dirname(path.dirname(path.abspath(__file__))) + '/data/brown_data.pk'
    brown_pickle = open(brown_file, 'wb')
    pickle.dump(brown_sents, brown_pickle)
    brown_pickle.close()

generateBrownPickle()


def generateTWSSPickle():

    '''
    Tokenize and pickle the TWSS sentences
    '''

    twss_sents_file = path.dirname(path.dirname(path.abspath(__file__))) + '/data/TWSS_sents.txt'
    twss_file = open(twss_sents_file)
    twss_sents = twss_file.readlines()
    twss_tokenized_sents = []

    # Tokenize the TWSS sentences and encode in ascii 
    for sent in twss_sents:
        tokenized_sent = TWT().tokenize(sent.strip())
        tokenized_sent = [token.decode('utf-8').encode('ascii', 'ignore') for token in tokenized_sent]
        twss_tokenized_sents.append(tokenized_sent)

    # Convert all sentences to lowercase
    for sent in twss_tokenized_sents:
        sent = [w.lower() for w in sent]

    twss_pickle_file = path.dirname(path.dirname(path.abspath(__file__))) + '/data/TWSS_data.pk'
    twss_pickle = open(twss_pickle_file, 'wb')
    pickle.dump(twss_tokenized_sents, twss_pickle)
    twss_pickle.close()

generateTWSSPickle()
