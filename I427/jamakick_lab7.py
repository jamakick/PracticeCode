#Jacob Kickbush jamakick
#Lab 5

import bs4, urllib.request, nltk, nltk.stem.porter as p, re, string
from nltk.corpus import stopwords
from collections import Counter


def createDict(urls, wordList):
    
    urlDict = {}
    
    pageNum = 1
    
    urls = urls[0:5]
    
    for url in urls:
        
        page = urllib.request.urlopen(url)
         
        pageContents = page.read().decode(errors="replace")
         
        page.close()
         
        content = bs4.BeautifulSoup(pageContents, "lxml")
        
        text = content.find_all(text = True)
        
        text = [piece.strip().lower() for piece in text if piece not in string.punctuation]
        
        wordCount = len(text)
        
        text = " ".join(text)
        
        urlDict[pageNum] = {"url" : url, "wordCount" : wordCount, "tfVector" : []}
        
        pageNum += 1
        
        tokens = nltk.word_tokenize(text)
    
        tokens = [word for word in tokens if word not in stopwords.words('english')]
        
        stemmer = p.PorterStemmer()
        
        stemList = [stemmer.stem(word) for word in tokens]
        #string.punctuation
        stemList = [word for word in stemList if not [letter for letter in word if letter in string.punctuation]]
     
        for word in stemList:
            if word not in wordList:
                wordList.append(word)
        
    return urlDict, wordList

def createVectors(urlDict, wordList):

    for i in range(5):
        
        url = urlDict[i+1]["url"]
        
        page = urllib.request.urlopen(url)
         
        pageContents = page.read().decode(errors="replace")
         
        page.close()
         
        content = bs4.BeautifulSoup(pageContents, "lxml")
        
        text = content.find_all(text = True)
        
        text = [piece.strip().lower() for piece in text if piece not in string.punctuation]
        
        text = [piece for piece in text if piece != '' or piece != ""]
        wordCounter = Counter(text)
        
        for word in wordList:
            urlDict[i+1]["tfVector"].append(wordCounter[word])
        
    return urlDict
            
def getUrls(url):
    
    try:
        page = urllib.request.urlopen(url)
    except:
        raise Exception("invalid page", url)
        
    else:
 
        pageContents = page.read().decode(errors="replace")
     
        page.close()
     
        content = bs4.BeautifulSoup(pageContents, "html.parser")
    
        hits = [link.get('href') for link in content.find_all('a', attrs={'href': re.compile("/wiki/")})]
    
        filters = ["http", "https", "Wikipedia", ".org", "Special:", "Help"]
     
        hits = [hit for hit in hits if not [exclude for exclude in filters if exclude in hit]]
        
        hits = ["https://en.wikipedia.org" + url for url in hits]
        
        return hits
    
def jaccardQuery(query, urlDict, wordList):
    
    rankedDict = {}
    
    query = query.split(" ")
    
    query = set(query)
    
    for i in range(5):
        
        document = set()
        
        for j in range(len(wordList)):
            if int(urlDict[i+1]["tfVector"][j]) > 0:
                document.add(wordList[j])
        jcIntersect = len(query.intersection(document))
        jcUnion = len(query.union(document))
        
        jaccardDistance = jcIntersect / jcUnion
        
        jaccardDistance = round((jaccardDistance * 1000), 3)
        
        
        rankedDict[jaccardDistance] = urlDict[i+1]["url"]
        
        rankedUrls = sorted(rankedDict.items(), reverse=True)
        
        rankedUrls = [(value, key) for (key, value) in rankedUrls]
        
    return rankedUrls

#seed links
links = getUrls("https://en.wikipedia.org/wiki/Phalanx")

wordList = []

urlDict, wordList = createDict(links, wordList)

urlDict = createVectors(urlDict, wordList)

results = jaccardQuery("search famine current user ashoka metadata", urlDict, wordList)

print("Jaccard Query Results, the pages and their scores are below. ")

for item in results:
    print(" page: " + str(item[0]) + "\n\tscore: " + str(item[1]))











#def getIndex(url, fullIndex):
#
#    page = urllib.request.urlopen(url)
# 
#    pageContents = page.read().decode(errors="replace")
# 
#    page.close()
# 
#    content = bs4.BeautifulSoup(pageContents, "lxml")
#
#    text = content.find_all(text = True)
#
#    text = [piece.strip().lower() for piece in text]
#
#    text = " ".join(text)
#
#    tokens = nltk.word_tokenize(text)
#
#    tokens = [word for word in tokens if word not in stopwords.words('english')]
#    
#    stemmer = p.PorterStemmer()
#    
#    stemList = [stemmer.stem(word) for word in tokens]
#    #string.punctuation
#    stemList = [word for word in stemList if not [letter for letter in word if letter in string.punctuation]]
#    
#    for term in stemList:
#        if term not in fullIndex:
#            fullIndex[term] = [url]
#        else:
#            if url not in fullIndex[term]:
#                fullIndex[term].append(url)
#            
#    return fullIndex



# text = [piece for piece in text if piece != '' or piece != ""]
# wordCounter = Counter(text)



#nltk.download('punkt')
#
#nltk.download('stopwords')


#for i in range(5):
#    fullIndex = getIndex(links[i], fullIndex)
#    
#print(fullIndex)
    
#sortedIndex = sorted([(len(value), key) for (key, value) in fullIndex.items()], reverse=True)[:100]
##
#print("Top 100 terms found in pages")
##
#for item in sortedIndex:
#    print(item[1], "has been found in ", item[0], "webpages.")
    
