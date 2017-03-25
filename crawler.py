import urllib2

seedLink = 'https://www.udacity.com/cs101x/index.html'
# seedLink='https://www.youtube.com'
searchMap = {}

'''This will populate the hashmap storing the keywords found on webpage and the links which contains
those keywords.'''


def populateSearchMap(uniqueWordsOnPage, link):
    global searchMap
    for word in uniqueWordsOnPage:
        word = word.strip()
        if not word:
            continue
        if word in searchMap:
            searchMap[word].append(link)
        else:
            searchMap[word] = [link]


def startCrawl(seedPage):
    # Set maximum number of pages to crawl
    maxPageCrawling = 10
    urls = [seedPage]
    crawlingIndex = 0
    # keep crawling until you get some number of links or no link left to crawl
    while maxPageCrawling > 0 and crawlingIndex < len(urls):
        url = getAllLinksInThePage(urls[crawlingIndex])
        mergeLists(urls, url)
        crawlingIndex += 1
        maxPageCrawling -= 1


# This will return a list having all the URLs listed in a page
def getAllLinksInThePage(link):
    urls = []
    if link.find('http') != 0:
        return urls
    try:
        content = urllib2.urlopen(link).read()
        copyContent = content
    except Exception, e:
        return urls
    while True:
        position = content.find('<a href=')
        if position < 0:
            populateSearchMap(extractTextContentOfPage(copyContent), link)
            return urls
        startPosition = content.find('"', position)
        endPosition = content.find('"', startPosition + 1)
        urls.append(content[startPosition + 1:endPosition])
        content = content[endPosition + 1:]


# Will merge the two lists and store result in first list
def mergeLists(resultUrls, urls):
    for url in urls:
        if url not in resultUrls:
            resultUrls.append(url)


# This will extract all the words from the page and return in a list
def extractTextContentOfPage(content):
    uniqueWordsOnPage = []
    while True:
        startPosition = content.find('>')
        endPosition = content.find('<', startPosition + 1)
        if startPosition < 0 or endPosition < 0:
            return uniqueWordsOnPage
        word = content[startPosition + 1:endPosition]
        if word not in uniqueWordsOnPage:
            mergeLists(uniqueWordsOnPage, word.split(' '))
        content = content[endPosition + 1:]


# Code which starts the crawler and populates the hashmap storing the inverted index
startCrawl(seedLink)
print searchMap
