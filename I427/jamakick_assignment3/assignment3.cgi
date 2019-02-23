#! /usr/bin/env python3

import cgi, cgitb, bs4, nltk, nltk.stem.porter as p, os, json, math

print('Content-type: text/html\n')

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

        with open(dirName + "/" + page, "r", encoding="utf8") as file:
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


def retrieve(queryTerms, invIndex):

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

    half = int(len(queryTerms) / 2)

    matchedPages = []

    termList = []

    completeMatch = []

    try:
        for term in queryTerms:
            pageMatch = invIndex[term]
            termList.append(pageMatch)

        for page in pageMatch:
            if page[0] not in matchedPages:
                matchedPages.append(page[0])

        for page in matchedPages:
            found = 0
            for outer in termList:
                for inner in outer:
                    if page in inner:
                        found += 1

            if found >= half:
                completeMatch.append(page)

        tf_idf = []

        for page in completeMatch:
            totalScore = 0
            for term in queryTerms:
                for allCounts in invIndex[term]:
                    if page in allCounts:
                        wordCount = allCounts[1]

                pageInfo = docDict[page]

                totalCount = pageInfo[0]

                ntf = int(wordCount) / int(totalCount)

                df = len(invIndex[term])

                idf = 1 / (1 + math.log(df))

                score = ntf * idf

                score *= 100000

                totalScore += score

            tf_idf.append([totalScore, pageInfo[2], pageInfo[1]])

        matchedPages = tf_idf

        matchedPages = [(link, title, score) for (score, link, title) in sorted(matchedPages, reverse=True)]

        if len(matchedPages) >= 25:
            matchedPages = matchedPages[0:25]
    except:
        matchedPages = None

    return matchedPages


form = cgi.FieldStorage()

cgitb.enable()

html = """
<!doctype html>
<html>
<head><meta charset='utf-8'>
<title>Searching Proto Recipe Search</title>
<meta http-equiv='x-ua-compatible' content='ie=edge'>
<meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>

<!--[if lte IE 9]>
	<p class='browserupgrade'>You are using an <strong>outdated</strong> browser. Please <a href='https://browsehappy.com/'>upgrade your browser</a> to improve your experience and security.</p>
<![endif]-->

<!-- Stylesheets -->
<link rel='stylesheet' href='css/normalize.css'>
<link rel='stylesheet' href='css/styles.css'>
<link href='https://fonts.googleapis.com/css?family=KoHo|Courgette' rel='stylesheet'>
</head>
    <body>
	<div id='cgi'>

	<h2>Proto Recipe Search</h2>

	<form action='assignment3.cgi' method='get'>
	<input type='text' name='queryTerms'>

	<input type='submit' value='Search'>
	</form>

	<h2>Results</h2>
	<ul>
	{0}
	</ul>
	</div>
    </body>
</html>"""

# nltk.download('punkt')

try:
    with open('invIndex.json', 'r', encoding="utf8") as invFile:
        invIndex = json.load(invFile)

    with open('docDict.json', 'r', encoding="utf8") as docFile:
        docDict = json.load(docFile)

except:
    invIndex, docDict = indexer("finalRun/parsedPages", "finalRun/index.dat")

    with open('invIndex.json', 'w', encoding="utf8") as invFile:
        json.dump(invIndex, invFile)

    with open('docDict.json', 'w', encoding="utf8") as docFile:
        json.dump(docDict, docFile)

queryTerms = form.getfirst("queryTerms", "html breakfast").split()


results = retrieve(queryTerms, invIndex)

output = ""
if results:

	for result in results:
		output += "<li>"
		output += "<a href='" + str(result[0]) + "'>" + str(result[1]) + "</a>"
		output += "<p>Score: " + str(result[2]) + "</p>"
		output += "</li>"
else:
	output +="<li>No Results Found</li>"

print(html.format(output.encode("utf8")))
