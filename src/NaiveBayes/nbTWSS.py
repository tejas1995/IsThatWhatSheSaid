import pickle 
import nltk

from os import sys, path
from nltk.tokenize.treebank import TreebankWordTokenizer as TWT

from unigramFeatures import *
from nbClassifier import *


if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from processData import splitTestTrainData


def trainTWSS(test=False):

    '''
    Retrieve training and test sentences and labels
    Build a vocabulary of words in the training sentences
    Extract unigram features for training and test sentences
    Train Naive Bayes classifier using training data
    Test classifier using test sentences
    '''

    brown_file = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/brown_data.pk'
    twss_file = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/TWSS_data.pk' 
    fml_file = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/FML_data.pk'
    tfln_file = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/TFLN_data.pk' 

    brown_train_sents, brown_train_y, brown_test_sents, brown_test_y = splitTestTrainData(brown_file, 0, 666)
    twss_train_sents, twss_train_y, twss_test_sents, twss_test_y = splitTestTrainData(twss_file, 1, 2000)
    fml_train_sents, fml_train_y, fml_test_sents, fml_test_y = splitTestTrainData(fml_file, 0, 666)
    tfln_train_sents, tfln_train_y, tfln_test_sents, tfln_test_y = splitTestTrainData(tfln_file, 0, 666)


    # Create training and test data by joining Brown and TWSS sets
    train_sents = brown_train_sents + twss_train_sents + fml_train_sents + tfln_train_sents
    train_y = brown_train_y + twss_train_y + fml_train_y + tfln_train_y
    test_sents = brown_test_sents + twss_test_sents + fml_test_sents + tfln_test_sents
    test_y = brown_test_y + twss_test_y + fml_test_y + tfln_test_y

    # Build vocalubary of words from training sentences
    wordset = buildWordset(train_sents)

    # Build unigram feature vector for training data
    train_X = extractFeatures(train_sents, wordset)

    # Train SVM classifier
    nb_classifier = classifier(train_X, train_y)

    if test is True:
 
        # Build bigram feature vector for test data
        test_X = extractFeatures(test_sents, wordset)

        # Predict and evaluate results for test data
        predicted_y = predict(nb_classifier, test_X)
        evaluate(predicted_y, test_y, test_sents)

    return nb_classifier, wordset


def predictTWSS(nb_classifier, wordset, list_sents):

    # Tokenize and preprocess sentences
    tokenized_sents = []
    for sent in list_sents:
        tokenized_sent = TWT().tokenize(sent.strip())
        tokenized_sent = [w.lower() for w in tokenized_sent]
        tokenized_sents.append(tokenized_sent)

    input_X = extractFeatures(tokenized_sents, wordset)
    twss_Y = predict(nb_classifier, input_X)
    return twss_Y


if __name__ == '__main__':
    trainTWSS(True)
