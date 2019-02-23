#I427 Lab 4
#Jake Kickbush user: jamakick

from collections import deque
from collections import Counter
import urllib.request, os, re, time

def getUrls(url):
    try:
        webPage = urllib.request.urlopen(url)
    except:
        print("That url doesn't work")
        return None
    else:
        webPage = urllib.request.urlopen(url)
        contents = webPage.read().decode(errors="replace")
        webPage.close()

        hits = re.findall('(?<=href=").+?(?=")', contents, re.DOTALL)

        filters = ["http", "https", "Wikipedia", ".org", "Special:", "Help"]

        hits = [hit for hit in hits if "/wiki/" in hit]

        hits = [hit for hit in hits if not [exclude for exclude in filters if exclude in hit]]
        

        return hits

def scrapeFrontier(frontier):

    for link in frontier:
        newLinks = getUrls(link)

        for link in newLinks:
            link = "https://en.wikipedia.org" + link
            if link not in frontier:
                frontier[link] = 1
            else:
                frontier[link] += 1

##        frontier.rotate()

        return frontier

seed = "https://en.wikipedia.org/wiki/Predator_X_(comics)"

totalLinksScraped = 0

start = time.clock()
#starting with the seed
frontier = Counter([seed])
print(frontier.most_common(20))

#scrape all the links from the frontier
frontier = scrapeFrontier(frontier)
print(frontier.most_common(20))
##
###scrape again for 3rd gen of links
frontier = scrapeFrontier(frontier)
print(frontier.most_common(20))

end = time.clock()
print("Total time is " + str(end - start))
print("Time per link is" + str((end - start) / len(frontier)))

#Version 1
##def getUrls(url):
##    
##    try:
##        webPage = urllib.request.urlopen(url)
##    except:
##        print("That url doesn't work")
##        return None
##    else:
##        webPage = urllib.request.urlopen(url)
##        contents = webPage.read().decode(errors="replace")
##        webPage.close()
##
##        hits = re.findall('(?<=href=").+?(?=")', contents, re.DOTALL)
##
##        filters = ["http", "https", "Wikipedia", ".org", "Special:", "Help"]
##
##        hits = [hit for hit in hits if "/wiki/" in hit]
##
##        hits = [hit for hit in hits if not [exclude for exclude in filters if exclude in hit]]
##
##        return hits
##
##def scrapeFrontier(frontier):
##
##    for link in frontier:
##        newLinks = getUrls(frontier[0])
##
##        for link in newLinks:
##            link = "https://en.wikipedia.org" + link
##            if link  not in frontier:
##                frontier.append(link)
##
####        frontier.rotate()
##
##        return frontier
##
##seed = "https://en.wikipedia.org/wiki/Predator_X_(comics)"
##
###starting with the seed
##frontier = deque([seed])
##print(frontier)
##
###scrape all the links from the frontier
##frontier = scrapeFrontier(frontier)
##print(frontier)
##
###scrape again for 3rd gen of links
##frontier = scrapeFrontier(frontier)
##print(frontier)
