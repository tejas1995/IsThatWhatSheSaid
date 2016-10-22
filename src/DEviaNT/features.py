import pickle
import nltk
import collections
from os import sys, path


if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def getDeviantFeatures():

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



getDeviantFeatures()
