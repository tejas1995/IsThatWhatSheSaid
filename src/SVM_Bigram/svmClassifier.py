from sklearn import svm

def classifier(train_X, train_y):

    '''
    Trains Naive Bayes classifier using training data
    '''
    
    print 'Training SVM classifier...'
    svmClassifier = svm.LinearSVC()
    svmClassifier.fit(train_X, train_y)
    return svmClassifier


def predict(classifier, test_X):

    '''
    Tests trained SVM classifier with test data
    '''

    print 'Predicting from test data...'
    pred_y = classifier.predict(test_X)
    return pred_y


def evaluate(pred_y, test_y, test_sents):

    '''
    Evaluates predictions of SVM classifier
    '''

    print 'Evaluating predictions...'
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for pred_val, test_val, sent in zip(pred_y, test_y, test_sents):
        if(pred_val == 1 and test_val == 1):
            TP += 1
        elif(pred_val == 1 and test_val == 0):
            FP += 1
            # print 'False Positive:', sent
        elif(pred_val == 0 and test_val == 1):
            FN += 1
            # print 'False Negative:', sent
        elif(pred_val == 0 and test_val == 0):
            TN += 1

    precision = float(TP)/(TP+FP)
    recall = float(TP)/(TP+FN)
    F_one = 2*precision*recall/(precision + recall)

    print 'Precision:', precision
    print 'Recall:', recall
    print 'F1 Score:', F_one

