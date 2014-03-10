from bs4 import BeautifulSoup
import urllib2
import urllib
from parserBase import *
import sys

class PirateproxyParser(TorrentParserBase):
	"""docstring for ClassName"""
	settings = TorrentParserSettings()
	settings.sitename = 'ThePirateBay'
	settings.base_uri = 'http://bayproxy.me/'
	settings.searchurl = settings.base_uri + 'search/'

	def _constructurl(self, keywords):
		search_string = ''.join(keywords)
		return self.settings.searchurl + urllib.quote_plus(search_string) + '/0/7/0'

	def _parsepage(self, page):
		soupPage = BeautifulSoup(page, 'lxml')
		searchResults = soupPage.find_all(id='searchResult')
		torrents = []
		try:
			for result in searchResults[0].find_all('tr'):
				searchResult = Torrent('The PirateBay')
				name = result.find(class_='detName')
				if(name is None):	# Not a torrent
					continue
				searchResult.name = name.get_text()
				for link in result.find_all('a'):
					if(link.get('class') and link.get('class')[0] == 'detLink'):
						searchResult.info_url = self.settings.base_uri + link.get('href')
					if(link.get('href').startswith('magnet')):
						searchResult.magnet_link = link.get('href')
						searchResult.has_magnet = True
				columns = result.find_all('td')
				searchResult.seeders = int(columns[2].get_text())
				searchResult.leechers = int(columns[3].get_text())
				torrents.append(searchResult)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			pass
		return torrents