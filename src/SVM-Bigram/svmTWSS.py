import pickle 
import nltk
from features import *
from svmClassifier import *
from os import sys, path

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
    train_sents = brown_train_sents + twss_train_sents + fml_train_sents + tfln_train_sents
    train_y = brown_train_y + twss_train_y + fml_train_y + tfln_train_y
    test_sents = brown_test_sents + twss_test_sents + fml_test_sents + tfln_test_sents
    test_y = brown_test_y + twss_test_y + fml_test_y + tfln_test_y

    print 'Number of training examples:', len(train_sents)
    print 'Number of testing examples:', len(test_sents)

    '''
    # Use the below for testing with unigram features

    # Build vocalubary of words from training sentences
    print "Building wordset..."	
    wordset = buildWordset(train_sents)

    # Build unigram feature vector for training data
    print "Extracting features for training data..."
    train_X = extractUnigramFeatures(train_sents, wordset)

    # Build unigram feature vector for test data
    print "Extracting features for test data..."
    test_X = extractUnigramFeatures(test_sents, wordset)
    '''

    # Building bigram vocabulary from training sentences
    print "Building bigram vocabulary..."
    bigramVocab = buildBigramVocab(train_sents)
 
    # Build bigram feature vector for training data
    print "Extracting features for training data..."
    train_X = extractBigramFeatures(train_sents, bigramVocab)

    # Train SVM classifier
    svm_classifier = classifier(train_X, train_y)

    if test is True:
 
        # Build bigram feature vector for test data
        print "Extracting features for test data..."
        test_X = extractBigramFeatures(test_sents, bigramVocab)

        # Predict and evaluate results for test data
        predicted_y = predict(svm_classifier, test_X)
        evaluate(predicted_y, test_y, test_sents)

    return svm_classifier


if __name__ == '__main__':
    trainTWSS(True)
