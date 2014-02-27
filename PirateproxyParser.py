from bs4 import BeautifulSoup
import urllib2
from parserBase import *

class PirateproxyParser(TorrentParserBase):
	"""docstring for ClassName"""
	settings = TorrentParserSettings()
	settings.sitename = 'ThePirateBay'
	settings.base_uri = 'http://bayproxy.me/'
	settings.searchurl = settings.base_uri + 'search/'

	def _constructurl(self, keywords):
		search_string = ' '.join(keywords)
		return self.settings.searchurl + search_string + '/0/7/0'

	def _parsepage(self, page):
		soupPage = BeautifulSoup(page)
		searchResults = soupPage.find_all(id='searchResult')
		torrents = []
		for result in searchResults[0].find_all('tr'):
			searchResult = Torrent()
			name = result.find(class_='detName')
			if(name is None):
				continue
			searchResult.name = name.get_text()
			for link in result.find_all('a'):
				if(link.get('class') == 'detLink'):
					searchResult.infoURL = link.get('href')
				if(link.get('href').startswith('magnet')):
					searchResult.magnetURL = link.get('href')
			torrents.append(searchResult)
		return torrents