Jacob Kickbush
Search Informatics Assignment 2


I am using a folder called part1Run that contains an example run of my Assignment1, inside
the folder is the index.dat file, and a folder called parsedPages, which includes all of the
downloaded html pages.

I also have the stopwords.txt file included, and then my indexer.py file which includes assignment 2 code

There are two functions included in my indexer.py file, the first is indexer()


indexer(dirName, indexFile)

indexer takes two arguments, the path to a directory of the downloaded html files, and a file name for my index.dat file
I open my stopwords file and read it in, and then do the same with my indexFile, while also putting it into a list for later use

I then create two empty dicts to hold my inverted index and my document info
I also get a list of all the contents of the dirName

iterate through every page in my dirName pages and read the file. I take the len of it right away for use in my docDict

I use beautiful soup to read it into a content, and then use .finds to get the header and title, cutting the ends off the title using indexing.

I then get the pageUrl by checking to see if my current page matches any of the indexed pages, and then saving that url to a variable

I then add an entry to my docDict for this page with these variables. 

I then tokenize and stem my content into a stemmedList

I create an entry for my term in the invIndex and set it to an empty list so I can append it later.

I then look at the set of my stemList, and for every term I append the page and the count of the term to the value of invIndex[term]

I then return my invIndex and docDict


my second function is retrieve()

retrieve(mode, queryTerms, invIndex):

my arguments are the mode, which is either "or", "and", or "most", my list of queryTerms to check,
and then the invIndex created from my indexer function

first I tokenize and stem my queryTerms the same way I did my content from my previous page. 

I then check to see what mode they use, if they use "or" then I look at every term in the queryTerms
and I pull out the pages and append them to the matched pages. This the results for or.

For and i do the same thing but I keep track of all the pages and all the terms. I then check for each page if it has every term using a inAll boolean variable.
It only appends the page to our matches if inAll remains true

Most is similar to and, but I use half the length of my queryTerms, and then count how many pages I find the terms in. 
If it is at least half of my terms length, then it is appended to the matched pages.

At the end of this I simply return my matched pages and print them out in the main.