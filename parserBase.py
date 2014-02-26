from bs4 import BeautifulSoup
import urllib2

class  TorrentParserSettings:
	pass

class Torrent:
	pass

class TorrentParserBase:

	def _constructurl(self, keywords):
		return 'http://bayproxy.me/search/test/0/7/'

	def _gethtmlpage(self, keywords):
		url = self._constructurl(keywords)
		u = urllib2.urlopen(url)
		contents = u.read()
		return contents

	def _parsepage(self, page):
		pass

	def findtorrents(self, keywords):
		htmlpage = self._gethtmlpage(keywords)
		self._parsepage(htmlpage)
