from bs4 import BeautifulSoup
import urllib2

class  TorrentParserSettings:
	base_uri 	= ''
	site_name	= ''
	search_url	= ''

	def __repr__(self):
		return u"<TorrentParserSettings: base_uri:%s site_name:%s>" % (self.base_uri, self.site_name)


class Torrent:
	name 		= ''
	infoURL 	= ''
	magnetURL 	= ''
	torrentURL	= ''

	def __repr__(self):
		return u"<Torrent: name:%s infoURL:%s magnetURL:%s>" % (self.name, self.infoURL, self.magnetURL)

class TorrentParserBase:

	def _constructurl(self, keywords):
		pass

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
