from bs4 import BeautifulSoup
import urllib2
from parserBase import *

class PirateproxyParser(TorrentParserBase):
	"""docstring for ClassName"""
	settings = TorrentParserSettings()
	settings.baseURI = 'http://bayproxy.me/search1.php?'

	def _parsepage(self, page):
		soupPage = BeautifulSoup(page)
		searchResults = soupPage.find_all(id='searchResult')
		print searchResults
		print "BLABL"
		for result in searchResults:
			print result.find_all(class_='detName')

	def _isSearchResult(tag):

		return True