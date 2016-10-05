from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import urllib
import nltk

list_TWSS_sents = []

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


for n in range(0, 200):
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
                setupLines = sent_detector.tokenize(jokeText[pos_quotes[-2]+1:pos_quotes[-1]].strip())
                for line in setupLines:
                    if len(line.split(' ')) >= 2:
                        list_TWSS_sents.append(line)

            except:
                continue

    except:
        continue


print len(list_TWSS_sents)

TWSS_file = open('../data/TWSS_sents.txt', 'w')
for line in list_TWSS_sents:
    TWSS_file.write(line.encode('utf-8')+'\n')
