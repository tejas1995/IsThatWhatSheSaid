import nltk
import pickle

from nltk.corpus import brown

def processBrownCorpusData():

    '''
    Retrieve 120 sentences from each category in the Brown corpus.
    Pickle the data
    '''

    brown_sents = []
    for cat in brown.categories():
        for sent in brown.sents(categories=cat)[:1220]:
            brown_sents.append(sent)

    brown_pickle = open('../data/brown_data.pk', 'wb')
    pickle.dump(brown_sents, brown_pickle)
    brown_pickle.close()

processBrownCorpusData()

