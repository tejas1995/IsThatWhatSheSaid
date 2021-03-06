from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
from os import path

import urllib
import nltk
import pickle

# Set base URLs
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"

# Sentence detector to split text into sentences
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


def makeSoup(url):

    hdr = {'User-Agent': user_agent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            }
    req = Request(url, headers=hdr)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "lxml")
    return soup


def getEroticaFileList():

    cats = ['0'] + [chr(x) for x in range(ord('A'), ord('Z')+1)]
    fileList = []

    for cat in cats:
        catUrl = 'http://textfiles.com/sex/EROTICA/' + cat + '/'
        print catUrl
        catSoup = makeSoup(catUrl)

        try:
            fileTRList = catSoup.find_all('tr', attrs={'valign': 'TOP'})
            for fileTR in fileTRList:
                fileLink = fileTR.find('a')['href']
                fileUrl = catUrl + fileLink
                fileList.append(fileUrl)            
        except:
            continue

    print len(fileList)
    return fileList


def retrieveEroticaFiles():
    
    fileList = getEroticaFileList()
    fileNumber = 0

    for fileUrl in fileList[:10]:
        try:
            testfile = urllib.URLopener()
            print fileUrl, fileNumber
            testfile.retrieve(fileUrl, '../data/EROTICA/'+str(fileNumber)+'.txt')
            fileNumber += 1
        except:
            continue

# retrieveEroticaFiles()


def processEroticaFiles():

    taggedEroticaList = []

    for fileNum in range(10):
        eroticaFile = open('../data/EROTICA/'+str(fileNum)+'.txt')
        sents = eroticaFile.readlines()
        # print sents
        preproc_sents = []
        for sent in sents:
            preproc_sent = sent.strip('\r\n')
            preproc_sent = preproc_sent.replace('\t', '')
            if len(preproc_sent) > 1:
                if not preproc_sent[-1] == ' ':
                    preproc_sent = preproc_sent + ' '
            preproc_sents.append(preproc_sent)
        full_text = ''.join(preproc_sents)
        text_sents = sent_detector.tokenize(full_text)

        # Tokenize and tag all sents in text_sents
        for sent in text_sents:
            tokenized_sent = nltk.tokenize.wordpunct_tokenize(sent)
            tagged_sent = nltk.pos_tag(tokenized_sent)
            taggedEroticaList.append(tagged_sent)

    erotica_file = path.dirname(path.dirname(path.abspath(__file__))) + '/data/erotica_data.pk'
    erotica_pickle = open(erotica_file, 'wb')
    pickle.dump(taggedEroticaList, erotica_pickle)
    erotica_pickle.close()





processEroticaFiles()
