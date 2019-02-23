#! /usr/bin/env python3

import cgi, ast, cgitb

print('Content-type: text/html\n')

form = cgi.FieldStorage()

cgitb.enable()

html = """
<!doctype html>
<html>
<head><meta charset='utf-8'>
<title>Searching Fake Google</title></head>
    <body>
	<p>Search Terms Given:</p>
	<p>{0}</p>
	<p>Urls that contain all search terms:</p>
	<ul>
	{1}
	</ul>
    </body>
</html>"""

searchTerms = form.getfirst("queryTerms", "outer space").split(" ")

try:
	termFile = open("termindex.txt", "r", encoding="utf-8")
	termContents = termFile.read()
	termFile.close()

	urlFile = open("urlindex.txt", "r", encoding="utf-8")
	urlContents = urlFile.read()
	urlFile.close()

	pagesUsed = []

	termContents = ast.literal_eval(termContents)
	urlContents = ast.literal_eval(urlContents)

	for term in searchTerms:
		if term in termContents:
			pagesUsed.append(set(termContents[term]))

	intersect = set(pagesUsed[0].intersection(*pagesUsed))

	urls = [urlContents[item] for item in intersect]

	printTerms = " ".join(searchTerms)
	printUrls = ""

	for url in urls:
		printUrls += "<li>" + url + "</li>"
except Exception as e:
	printTerms = "The code was unsuccessful in running"
	printUrls = e


print(html.format(printTerms, printUrls))
