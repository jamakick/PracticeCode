import bs4, nltk, nltk.stem.porter as p, os


def indexer(dirName, indexFile):
    
    with open("stopwords.txt", "r", encoding="utf8") as stopwordFile:
        stopwords = stopwordFile.read()
    
    with open(indexFile, "r", encoding="utf8") as indexFile:
        indexContent = indexFile.readlines()
        
    indexContent = [item.split(" ") for item in indexContent]
        
    pages = os.listdir(dirName)

    invIndex = {}
    
    docDict = {}
    
    for page in pages:
    
        with open("foodRun/parsedPages/" + page, "r", encoding="utf8") as file:
            pageContents = file.read()
 
        contentLen = len(pageContents)
        
        content = bs4.BeautifulSoup(pageContents, "lxml")

        header = content.find('head')
        
        title = str(header.find('title'))[7:-8]
        
        pageUrl = ""
        
        for fileName in indexContent:
            if fileName[0] == page:
                pageUrl = fileName[1].strip()
                
        docDict[page] = [contentLen, title, pageUrl]

        text = content.find_all(text = True)

        text = [piece.strip().lower() for piece in text]

        text = " ".join(text)

        tokens = nltk.word_tokenize(text)

        tokens = [word for word in tokens if word not in stopwords]
    
        stemmer = p.PorterStemmer()
    
        stemList = [stemmer.stem(word) for word in tokens]
    
        stemList = [word for word in stemList if not [letter for letter in word if letter in "][%;/({:})`.',?!\""]]


        for term in stemList:
            if term not in invIndex:
                invIndex[term] = []

        for term in set(stemList):
            
            termList = [page, stemList.count(term)]
            
            if termList not in invIndex[term]:
                invIndex[term].append(termList)
            
    return invIndex, docDict


def retrieve(mode, queryTerms, invIndex):
    
    with open("stopwords.txt", "r", encoding="utf8") as stopwordFile:
        stopwords = stopwordFile.read()
    
    text = [piece.strip().lower() for piece in queryTerms]

    text = " ".join(text)

    tokens = nltk.word_tokenize(text)

    tokens = [word for word in tokens if word not in stopwords]

    stemmer = p.PorterStemmer()

    stemList = [stemmer.stem(word) for word in tokens]

    stemList = [word for word in stemList if not [letter for letter in word if letter in "][%;/({:})`.',?!\""]]

    queryTerms = stemList
    
    if mode == 'or':
        
        matchedPages = []
        
        for term in queryTerms:
            
            pageMatch = invIndex[term]
            
            for page in pageMatch:
                if page not in matchedPages:
                    matchedPages.append(page[0])        
            
    elif mode == 'and':
        matchedPages = []
        
        termList = []
        
        completeMatch = []
        
        for term in queryTerms:
            
            pageMatch = invIndex[term]
            termList.append(pageMatch[0])
            
            for page in pageMatch:
                if page not in matchedPages:
                    matchedPages.append(page[0])  
                
        for page in matchedPages:
            inAll = True
            for lst in termList:
                if page not in lst:
                    inAll = False
            
            if inAll:
                completeMatch.append(page)
                
        matchedPages = completeMatch
        
    elif mode == 'most':
        
        half = int(len(queryTerms) / 2)
        
        matchedPages = []
        
        termList = []
        
        completeMatch = []
        
        for term in queryTerms:
            
            pageMatch = invIndex[term]
            termList.append(pageMatch[0])
            
            for page in pageMatch:
                if page not in matchedPages:
                    matchedPages.append(page[0])  
                
        for page in matchedPages:
            found = 0
            for lst in termList:
                if page in lst:
                    found += 1
            
            if found >= half:
                completeMatch.append(page)
                
        matchedPages = completeMatch
    else:
        return "That was not a valid mode"
    
    return matchedPages
    
invIndex, docDict = indexer("foodRun/parsedPages", "foodRun/index.dat")


#matchedPages = retrieve("or", ["previous", "team1", "dpbrugler"], invIndex)

#for page in matchedPages:
#    print(str(docDict[page][1]) + "  " + str(docDict[page][2]))