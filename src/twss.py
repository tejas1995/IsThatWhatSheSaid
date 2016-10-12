from NaiveBayes import nbTWSS
from SVM_Bigram import svmTWSS

inp = ''
typ_clf = ''

print 'Which version of Michael Scott would you like to meet?'
print "A: Nichael Bott. He's kinda dumb"
print "B: Scott Von Michael. He's also dumb, but less so."

while(True):
    typ_clf = raw_input('> ')

    # Train classifier for selected Michael Scott
    if(typ_clf == 'A'):
        print "Waking up Nichael Bott..."
        clf, vocab = nbTWSS.trainTWSS()
        predictor = nbTWSS.predictTWSS
        break
    elif(typ_clf == 'B'):
        print "Waking up Scott Von Michael..."
        clf, vocab = svmTWSS.trainTWSS()
        predictor = svmTWSS.predictTWSS
        break

while(True):

    inp = raw_input('>> ')
    if inp == 'q':
        break

    # Predict if input is a TWSS with selected classifier
    twss_res = predictor(clf, vocab, [inp])
    if twss_res[0] == 1:
        print "That's what she said!"
    else:
        print "..."
