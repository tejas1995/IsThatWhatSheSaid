from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import urllib


# Set base URLs
user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"

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

    for fileUrl in fileList[:1000]:
        try:
            testfile = urllib.URLopener()
            print fileUrl, fileNumber
            testfile.retrieve(fileUrl, '../data/EROTICA/'+str(fileNumber)+'.txt')
            fileNumber += 1
        except:
            continue

retrieveEroticaFiles()    
