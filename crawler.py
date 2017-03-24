#First get a seed page
#Call a method startCrawl() on the seed link
#keep crawling until you get some number of links or no link left to crawl
#Use some helper methods
import urllib2

seedLink=''

def startCrawl(seedPage):
	maxPageCrawling = 100
	urls = [seedPage]
	crawlingIndex = 0
	while maxPageCrawling > 0 and crawlingIndex < len(urls):
		url = getAllLinksInThePage(urls[crawlingIndex])
		mergeLists(urls,url)
		crawlingIndex += 1
	print urls


def getAllLinksInThePage(link):
	urls = []
	content = urllib2.urlopen(link).read()
	while True:
		position = content.find('<a href=')
		if position < 0:
			return urls
		startPosition = content.find('"',position)
		endPosition = content.find('"',startPosition+1)
		urls.append(content[startPosition+1:endPosition])
		content = content[endPosition+1:]
	return urls


def mergeLists(resultUrls,urls):
	for url in urls:
		if url not in resultUrls:
			resultUrls.append(url)

#Main
startCrawl(seedLink) 
