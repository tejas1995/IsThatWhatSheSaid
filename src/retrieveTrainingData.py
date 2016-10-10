from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import urllib
import nltk
import ctypes
import sys


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

    
def retrieveTWSSData():

    '''
    Retrieves as many (upto 240) stories as possible from
    TWSSstories.com
    '''
    list_TWSS_sents = []

    for n in range(0, 240):
        print n

        url = "http://twssstories.com/node?page=" + str(n)
        soup = makeSoup(url)

        # for i in range(10):

        try:
            jokeDivList = soup.find_all(attrs={'class': 'content clear-block'})
            for jokeDiv in jokeDivList:

                jokeText = jokeDiv.find('p').string
                try:
                    pos_quotes = [pos for pos, char in  enumerate(jokeText) if char == '"']
                    joke = jokeText[pos_quotes[-2]+1:pos_quotes[-1]].strip()
                    if len(joke.split(' ')) >= 2:
                        list_TWSS_sents.append(joke)

                except:
                    continue

        except:
            continue


    print len(list_TWSS_sents)

    TWSS_file = open('../data/TWSS_sents.txt', 'w')
    for line in list_TWSS_sents:
        TWSS_file.write(line.encode('utf-8')+'\n')


def retrieveTFLNData():

    '''
    Retrieves upto 1400 texts  from
    www.TextsFromLastNight.com
    '''

    list_TFLN_sents = []

    for n in range(1, 101):
        print n

        url = "http://www.textsfromlastnight.com/texts/page:" + str(n)
        soup = makeSoup(url)

        try:
            textDivList = soup.find_all(attrs={'class': 'content'})
            for textDiv in textDivList:
                textStr = textDiv.find('p').string
                if 'Text' in textStr and 'Last' in textStr and 'Night' in textStr:
                    continue
                else:
                    list_TFLN_sents.append(textStr) 

        except:
            continue
        
    # print len(list_TFLN_sents)

    TFLN_file = open('../data/TFLN_sents.txt', 'w')
    for line in list_TFLN_sents:
        TFLN_file.write(line.encode('utf-8')+'\n')


def retrieveFMLData():

    '''
    Retrieves upto  entries from
    www.fmylife.com/intimacy
    '''

    list_FML_sents = []

    for n in range(1, 109):
        print n

        url = "http://www.fmylife.com/intimacy?page=" + str(n) + "#top"
        soup = makeSoup(url)

        try:

            fmlDivList = soup.find_all(attrs={'class': 'post article cat-intimacy'})
            fmlDivList += soup.find_all(attrs={'class': 'post article is-spicy cat-intimacy'})
            for fmlDiv in fmlDivList:
                fmlStr = fmlDiv.find('p', attrs={'class': 'content'}).string
                list_FML_sents.append(fmlStr)

        except:
            continue


    FML_file = open('../data/FML_sents.txt', 'w')
    for line in list_FML_sents:
        FML_file.write(line.encode('utf-8')+'\n')


if __name__ == '__main__':
    
    if 'TWSS' in sys.argv:
        retrieveTWSSData()
    if 'TFLN' in sys.argv:
        retrieveTFLNData()
    if 'FML' in sys.argv:
        retrieveFMLData()

