import pickle 
import nltk

def splitTestTrainData(filename, is_twss):

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
    b_train_sents, b_train_y, b_test_sents, b_test_y = splitTestTrainData('../../data/brown_data.pk', 0)
    t_train_sents, t_train_y, t_test_sents, t_test_y = splitTestTrainData('../../data/TWSS_data.pk', 1)

    print len(b_train_sents), len(b_train_y), len(t_train_sents), len(t_train_y)

    train_sents = b_train_sents + t_train_sents
    train_y = b_train_y + t_train_y
    test_sents = b_test_sents + t_test_sents 
    test_y = b_test_y + t_test_y

    wordset = buildWordset(train_sents)
    train_X = extractFeatures(train_sents, wordset)     # Build unigram feature vector for training data
    test_X = extractFeatures(test_sents, wordset)       # Build unigram feature vector for test data

    svm_classifier = classifier(train_X, train_y)
    predicted_y = predict(classifier, test_y)
    evaluate(predicted_y, test_y)

if __name__ == '__main__':
    twss()
