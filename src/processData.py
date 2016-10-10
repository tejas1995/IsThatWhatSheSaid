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


def generatePickleFromTxt(type_sents):

    '''
    Tokenize and pickle the TWSS sentences
    '''

    sents_filename = path.dirname(path.dirname(path.abspath(__file__))) + '/data/' + type_sents + '_sents.txt'
    sents_file = open(sents_filename)
    sents = sents_file.readlines()
    tokenized_sents = []

    # Tokenize the TWSS sentences and encode in ascii 
    for sent in sents:
        tokenized_sent = TWT().tokenize(sent.strip())
        tokenized_sent = [token.decode('utf-8').encode('ascii', 'ignore') for token in tokenized_sent]
        tokenized_sents.append(tokenized_sent)

    # Convert all sentences to lowercase
    for sent in tokenized_sents:
        sent = [w.lower() for w in sent]

    pickle_file = path.dirname(path.dirname(path.abspath(__file__))) + '/data/' + type_sents + '_data.pk'
    text_pickle = open(pickle_file, 'wb')
    pickle.dump(tokenized_sents, text_pickle)
    text_pickle.close()


def splitTestTrainData(filename, is_twss, size_training):

    '''
    split the training data by using first size_training sentences of given file as training data and rest as test data
    '''
    train_sents = []
    train_y = []

    test_sents = []
    test_y = []

    pickle_file = open(filename)
    sents = pickle.load(pickle_file)
    for sent in sents[:size_training]:
        train_sents.append(sent)
        train_y.append(is_twss)
    for sent in sents[size_training:]:
        test_sents.append(sent)
        test_y.append(is_twss)
    pickle_file.close()

    return train_sents, train_y, test_sents, test_y


if __name__ == '__main__':
    generateBrownPickle()
    generatePickleFromTxt('TWSS')
    generatePickleFromTxt('TFLN')
    generatePickleFromTxt('FML')
