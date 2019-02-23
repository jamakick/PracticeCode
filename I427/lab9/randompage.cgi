#! /usr/bin/env python3

import cgi, ast, cgitb, random, urllib.request

print('Content-type: text/html\n')

cgitb.enable()

try:
	urlFile = open("urlindex.txt", "r", encoding="utf-8")
	urlContents = urlFile.read()
	urlFile.close()

	urlContents = ast.literal_eval(urlContents)

	randomPage = random.choice(list(urlContents.values()))

	web_page = urllib.request.urlopen(randomPage)
	contents = web_page.read().decode(errors="replace")
	web_page.close()

except Exception as e:
	contents = "Random web page could not be found. ", e

print(contents.encode("utf-8"))
