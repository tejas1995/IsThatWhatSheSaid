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


b_train_sents, b_train_y, b_test_sents, b_test_y = splitTestTrainData('../../data/brown_data.pk', 0)
t_train_sents, t_train_y, t_test_sents, t_test_y = splitTestTrainData('../../data/TWSS_data.pk', 1)

print len(b_train_sents), len(b_train_y), len(t_train_sents), len(t_train_y)

train_sents = b_train_sents + t_train_sents
train_y = b_train_y + t_train_y
test_sents = b_test_sents + t_test_sents 
test_y = b_test_y + t_test_y

print 'Len of train_sents:', len(train_sents)
print 'Len of train_y:', len(train_y)
print 'Len of test_sents:', len(test_sents)
print 'Len of test_y:', len(test_y)



