#Jacob Kickbush jamakick/
#Lab 6

import bs4, urllib.request, nltk, nltk.stem.porter as p, re
from nltk.corpus import stopwords


def getIndex(url, fullIndex, urlDict):

    page = urllib.request.urlopen(url)
 
    pageContents = page.read().decode(errors="replace")
 
    page.close()
 
    content = bs4.BeautifulSoup(pageContents, "lxml")

    text = content.find_all(text = True)

    text = [piece.strip().lower() for piece in text]

    text = " ".join(text)

    tokens = nltk.word_tokenize(text)

    tokens = [word for word in tokens if word not in stopwords.words('english')]
    
    stemmer = p.PorterStemmer()
    
    stemList = [stemmer.stem(word) for word in tokens]
    
    stemList = [word for word in stemList if not [letter for letter in word if letter in "][%;/({:})`.',?!\""]]
    
    for term in stemList:
        if term not in fullIndex:
            fullIndex[term] = [len(urlDict) + 1]
        else:
            if (len(urlDict) + 1) not in fullIndex[term]:
                fullIndex[term].append(len(urlDict) + 1)
                
    
    urlDict[len(urlDict) + 1] = url
            
    return fullIndex, urlDict
            
def getUrls(url):
    try:
        page = urllib.request.urlopen(url)
    except:
        print("invalid page", url)
        return None
    else:
 
        pageContents = page.read().decode(errors="replace")
     
        page.close()
     
        content = bs4.BeautifulSoup(pageContents, "lxml")
    
        hits = [link.get('href') for link in content.find_all('a', attrs={'href': re.compile("/wiki/")})]
    
        filters = ["http", "https", "Wikipedia", ".org", "Special:", "Help"]
     
        hits = [hit for hit in hits if not [exclude for exclude in filters if exclude in hit]]
        
        return hits
    
def searchIndex(fullIndex, urlDict):
    print("Prototype Index Search: ")
    searchTerms = input("Please enter search terms, separated by spaces. ex: outer space \n Enter Here: ")

    try:
        terms = searchTerms.split(" ")
    
        commonList = []
    
        for term in terms:
            commonList.append(fullIndex[term])

        commonality = set.intersection(*map(set, commonList))
        
    except:
        print("There are no pages that match the intersection of " + searchTerms + ", try again.")
    
    else:
        print("These are the pages found that match your query. \n")
    
        if commonality:
            for commonTerm in list(commonality):
                print(urlDict[commonTerm])
        else:
            print("There were no pages found that match the intersection of " + searchTerms + ", try again.")

#seed links
links = getUrls("https://en.wikipedia.org/wiki/Outer_space")
links = ["https://en.wikipedia.org" + url for url in links]
fullIndex = {}

urlDict = {}

for i in range(10):
    if links[i] not in urlDict.values():
        fullIndex, urlDict = getIndex(links[i], fullIndex, urlDict)

#searchIndex(fullIndex, urlDict)

print("fullIndex")
print(fullIndex)

print("urlDict")
print(urlDict)
    

#nltk.download('punkt')
#
#nltk.download('stopwords')   
    
#print out the most common terms and how many pages were found
#sortedIndex = sorted([(len(value), key) for (key, value) in fullIndex.items()], reverse=True)[0:100]
#
#print("Top 100 terms found in pages")
#
#for item in sortedIndex:
#    print(item[1], "has been found in ", item[0], "webpages.")
#    
