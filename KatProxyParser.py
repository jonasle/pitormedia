from bs4 import BeautifulSoup
import urllib2
import urllib
from parserBase import *
import sys

class KatProxyParser(TorrentParserBase):
	"""docstring for ClassName"""
	settings = TorrentParserSettings()
	settings.sitename = 'Kickass Torrents'
	settings.base_uri = 'http://katproxy.com/'
	settings.searchurl = settings.base_uri + 'usearch/'

	def _constructurl(self, keywords):
		search_string = ''.join(keywords)
		return self.settings.searchurl + urllib.quote_plus(search_string)

	def _parsepage(self, page):
		soupPage = BeautifulSoup(page)
		searchResults = soupPage.find_all(class_='data')
		torrents = []
		try:
			for result in searchResults[0].find_all('tr'):
				searchResult = Torrent(self.settings.sitename)
				name = result.find(class_='torrentname')
				if(name is None):	# Not a torrent
					continue
				searchResult.name = name.get_text()
				for link in result.find_all('a'):
					if(link.get('class') and link.get('class')[0] == 'torType'):
						searchResult.info_url = self.settings.base_uri + link.get('href')
					if(link.get('class') and link.get('class')[0] == 'idownload'):
						searchResult.torrent_url = link.get('href')
						searchResult.has_torrent = True
					if(link.get('href').startswith('magnet')):
						searchResult.magnet_link = link.get('href')
						searchResult.has_magnet = True
				seeders = result.find(class_='green')
				if(seeders is not None):
					searchResult.seeders = int(seeders.get_text())
				torrents.append(searchResult)
		except:
			print "Unexpected error:", sys.exc_info()
			pass
		return torrents