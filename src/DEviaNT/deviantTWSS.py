import pickle 
import nltk

from os import sys, path
from nltk.tokenize import wordpunct_tokenize as WPT

from features import *
from svmClassifier import *


if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from processData import splitTestTrainData


def trainTWSS(test=False):

    '''
    Retrieve training and test sentences and labels
    Build a vocabulary of words in the training sentences
    Extract bigram features for training and test sentences
    Train SVM classifier using training data
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
    ut_train_sents = brown_train_sents + twss_train_sents + fml_train_sents + tfln_train_sents
    ut_train_y = brown_train_y + twss_train_y + fml_train_y + tfln_train_y
    ut_test_sents = brown_test_sents + twss_test_sents + fml_test_sents + tfln_test_sents
    ut_test_y = brown_test_y + twss_test_y + fml_test_y + tfln_test_y


    # Tag train_X
    train_sents = []
    train_y = []
    for sent, y in zip(ut_train_sents, ut_train_y):
        try:
            tagged_sent = nltk.pos_tag(sent)
            train_sents.append(tagged_sent)
            train_y.append(y)
        except:
            continue

    # Tag test_X
    test_sents = []
    test_y = []
    for sent, y in zip(ut_test_sents, ut_test_y):
        try:
            tagged_sent = nltk.pos_tag(sent)
            test_sents.append(tagged_sent)
            test_y.append(y)
        except:
            continue


    # Build DEviaNT feature vector for training data
    train_X = extractDeviantFeatures(train_sents)

    # Train SVM classifier
    svm_classifier = classifier(train_X, train_y)

    if test is True:
 
        # Build bigram feature vector for test data
        test_X = extractDeviantFeatures(test_sents)

        # Predict and evaluate results for test data
        predicted_y = predict(svm_classifier, test_X)
        evaluate(predicted_y, test_y, test_sents)

    return svm_classifier


def predictTWSS(svm_classifier, list_sents):

    # Tokenize and tagged sentences
    processed_sents = []
    for sent in list_sents:
        tokenized_sent = WPT(sent.strip())
        tokenized_sent = [w.lower() for w in tokenized_sent]
        tagged_sent = nltk.pos_tag(tokenized_sent)
        processed_sents.append(tagged_sent)

    input_X = extractDeviantFeatures(tokenized_sents)
    twss_Y = predict(svm_classifier, input_X)
    return twss_Y


if __name__ == '__main__':
    trainTWSS(True)
