import pickle 
import nltk
from bigramFeatures import *
from svmClassifier import *
from os import sys, path

if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from processData import splitTestTrainData


def twss():

    '''
    Retrieve training and test sentences and labels
    Build a vocabulary of words in the training sentences
    Extract bigram features for training and test sentences
    Train SVM classifier using training data
    Test classifier using test sentences
    '''

    brown_file = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/brown_data.pk'
    twss_file = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/TWSS_data.pk' 

    b_train_sents, b_train_y, b_test_sents, b_test_y = splitTestTrainData(brown_file, 0, 2000)
    t_train_sents, t_train_y, t_test_sents, t_test_y = splitTestTrainData(twss_file, 1, 2000)

    # Create training and test data by joining Brown and TWSS sets
    train_sents = b_train_sents + t_train_sents
    train_y = b_train_y + t_train_y
    test_sents = b_test_sents + t_test_sents 
    test_y = b_test_y + t_test_y

    print 'Number of training examples:', len(train_sents)
    print 'Number of testing examples:', len(test_sents)

    # Build vocalubary of words from training sentences
    print "Building wordset..."	
    wordset = buildWordset(train_sents)

    # Build unigram feature vector for training data
    print "Extracting features for training data..."
    train_X = extractFeatures(train_sents, wordset)

    # Build unigram feature vector for test data
    print "Extracting features for test data..."
    test_X = extractFeatures(test_sents, wordset)

    # Classify, predict, evaluate
    svm_classifier = classifier(train_X, train_y)
    predicted_y = predict(svm_classifier, test_X)
    evaluate(predicted_y, test_y, test_sents)

if __name__ == '__main__':
    twss()
