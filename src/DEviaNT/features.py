import pickle
import nltk
import collections
from os import sys, path


if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def extractDeviantFeatures(list_sents):

    sent_features = []

    # load SN list
    SN_filename = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/SN.txt'
    SN_list = open(SN_filename).readlines()
    SN_list = [s.strip() for s in SN_list]
    print SN_list

    # Load BP list
    BP_filename = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/BP.txt'
    BP_list = open(BP_filename).readlines()
    BP_list = [s.strip() for s in BP_list]
    print BP_list

    # Load tagged erotica
    erotica_filename = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + '/data/erotica_data.pk'
    erotica_file = open(erotica_filename)
    erotica_list = pickle.load(erotica_file)
    for erotica_sent in erotica_list[:10]:
        print erotica_sent

    # Define tag lists for nouns, verbs and adjectives
    nounTagList = ['NN', 'NNP', 'NNPS', 'NNS']
    verbTagList = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    adjTagList = ['JJ', 'JJR', 'JJS']
    punctTagList = ['$', "''", '(', ')', ',', '--', '.', ':']

    # Define features for every sentence in list_sents
    for s in list_sents:

        s_features = []


        # NOUN-EUPHEMISM features
        # Does s contain a noun belonging to SN?
        nounInSNFtr = 0
        for token in s:
            if token[1] in nounTagList:
                if token[0] in SN_list:
                    nounInSNFtr = 1
        print nounInSNFtr
        s_features.append(nounInSNFtr)

        # Does s contain a noun belonging to BP?
        nounInBPFtr = 0
        for token in s:
            if token[1] in nounTagList:
                if token[0] in BP_list:
                    nounInBPFtr = 1
        print nounInBPFtr
        s_features.append(nounInBPFtr)

        # STRUCTURAL features
        numPunctTokens = 0
        numNonPunctTokens = 0
        for token in s:
            if token[1] in punctTagList:
                numPunctTokens += 1
            else:
                numNonPunctTokens += 1
        s_features.append(numPunctTokens)
        s_features.append(numNonPunctTokens)


        sent_features.append(s_features)

    return sent_features


extractDeviantFeatures([])
