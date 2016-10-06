import pickle 
import nltk

from unigramFeatures import *
# from NBClassifier import *


def splitTestTrainData(filename, is_twss):

    '''
    split the training data by using last 100 sentences of given file as test data
    '''
    train_sents = []
    train_y = []

    test_sents = []
    test_y = []

    pickle_file = open(filename)
    sents = pickle.load(pickle_file)
    for sent in sents[:-100]:
        train_sents.append(sent)
        train_y.append(is_twss)
    for sent in sents[-100:]:
        test_sents.append(sent)
        test_y.append(is_twss)
    pickle_file.close()

    return train_sents, train_y, test_sents, test_y


def twss():

    '''
    Retrieve training and test sentences and labels
    Build a vocabulary of words in the training sentences
    Extract unigram features for training and test sentences
    Train Naive Bayes classifier using training data
    Test classifier using test sentences
    '''

    b_train_sents, b_train_y, b_test_sents, b_test_y = splitTestTrainData('../../data/brown_data.pk', 0)
    t_train_sents, t_train_y, t_test_sents, t_test_y = splitTestTrainData('../../data/TWSS_data.pk', 1)

    # print len(b_train_sents), len(b_train_y), len(t_train_sents), len(t_train_y)

    train_sents = b_train_sents + t_train_sents
    train_y = b_train_y + t_train_y
    test_sents = b_test_sents + t_test_sents 
    test_y = b_test_y + t_test_y

    for sent in train_sents:
        for w in sent:
            try:
                w.decode('ascii')
            except UnicodeDecodeError:
                print w, 'was not an ascii-encoded unicode string'
                print sent
                print isinstance(w, str), ',', isinstance(w, unicode)
            else:
                continue

    print "Building wordset..."	
    wordset = buildWordset(train_sents)
    print "Extracting features for training data..."
    train_X = extractFeatures(train_sents, wordset)     # Build unigram feature vector for training data
    print "Extraction features for test data..."
    test_X = extractFeatures(test_sents, wordset)       # Build unigram feature vector for test data

    # svm_classifier = classifier(train_X, train_y)
    # predicted_y = predict(classifier, test_y)
    # evaluate(predicted_y, test_y)

if __name__ == '__main__':
    twss()
