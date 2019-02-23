Jacob Kickbush jamakick
Readme for Programming Assignment 1

Example variables used to run depth first search

python assignment1.py "https://www.cnn.com/" 50 part1Run bfs

Example variables used to run breadth first search
python assignment1.py "https://www.cnn.com/" 50 bfsTestRun 

assignment1.py --> name of the script

"https://www.cnn.com/" --> seed url

50 --> max number of web pages crawled

dfsTestRun --> folder name of where you want the files saved. It will be saved in the same directory as the python file.

dfs --> type of search, dfs is depth first, bfs is breadth first


Functions:

validVars() -- this function looks at the arguments given in sys.argv and checks
if the variable given were in the right position and format, otherwise it throws and exception

webCrawler(url, maxPages, saveLoc, searchType) -- Tries to open the seed url and retrieve its contents
writes the seed file out as 0.html and then uses bs4 to find all the links in the contents
check for duplicates and turn it into a deque so we can use popleft, start our indexDict with the seed,
for the range of our maxPages, we check to see if they are using depthfirst or breadthfirst
If we are using depth first, we pop until we find a url that hasn't been crawled yet.
We then use the robot parser and urlparse to check if there is a robots.txt file and if we can
open our current url or not. If we can't, then it moves on to the next link, if we can then we open the url,
get the contents, write to a file that is saved as the len of the indexDict.html and then get all the links and add them to our links list at the end, checking for dupes.
we also use the time.sleep() function here to slow down our request speed
for breadth first we do the same thing except we popleft instead of popping right.

we return our indexDict at the end, and then write it out to a index.dat file

