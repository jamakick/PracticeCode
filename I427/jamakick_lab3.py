#I427 Lab 3
#Jake Kickbush user: jamakick

import urllib.request, os, re

def getUrls():
    #empty list of urls that we will append them to
    urls = []
    htmlFiles = []

    #loop
    while True:
        #ask user for url input
        url = input("Please provide a URL or type 'done': ")

        #checks if the input entered was 'done'
        if url.lower() == "done":
            output = input("Print most recent link ('new'), least recent ('old'), or all links ('all')? ")

            #if they enter new, they get the newest link and it is removed from our list of links
            if output.lower() == "new":
                print(urls[-1])
                urls.remove(urls[-1])
                break
            #if they enter old, they get the oldest link and it is removed from the list of links
            elif output.lower() == "old":
                print(urls[0])
                urls.remove(urls[0])
                break
            #if they enter all, or anything else, it will print out all the urls
            else:
                print("URLS in list: " + str(len(urls)))
                for url in urls:
                    print("  " + url)
                break

        #checks to see if the url is already in our list or not    
        if url not in urls:
            #try except statement checks to see if it is a url or not,
            #if it isn't then it isn't added to the list
            try:
                webPage = urllib.request.urlopen(url)
            except:
                print("That is not a valid url")
            else:
                urls.append(url)

    #downloads all the html files
    print("Downloading urls to files")

    #opens every url
    for url in urls:
        webPage = urllib.request.urlopen(url)
        contents = webPage.read().decode(errors="replace")
        webPage.close()

        #checks if the url has a basename or not, if it does then its called that
        if os.path.basename(url):
            fileName = os.path.basename(url)
        else:
            #if there is no basename, we use page and add the index and .html, so they don't overwrite
            fileName = "page" + str(urls.index(url)) + ".html"

        #we add to the list of filenames so we can return them
        htmlFiles.append(fileName)

        #writes out the html files
        fileOut = open(fileName, "w", encoding="utf-8")
        fileOut.write(contents)
        fileOut.close()

    #clears our urls, deleting them now that the file has been created
    urls =  []

    #prints out the files that have been created
    print("Files created:")
    for name in htmlFiles:
        print("  " + name)

    #we return the filenames of our html pages
    return htmlFiles


#main
fileNames = getUrls()

#holds every single link from all the pages we downloaded
links = []

#for every filename from our returned list
for fileName in fileNames:
    #read in the contents of the html file
    file = open(fileName, "r", encoding="utf-8")
    contents = file.read()
    file.close()

    #regular expression to find every single link, looking behind href=" and ahead of a "
    #we use dotall here so that we look through the entire html page and not just one line
    hits = re.findall('(?<=href=").+?(?=")', contents, re.DOTALL)

    #we add every hit to our links list so that all of the links from every page are together
    for hit in hits:
        links.append(hit)


#print out the links found on all the pages together
print("List of all links in the HTML pages found")

for link in links:
    print("  " + link)
    
