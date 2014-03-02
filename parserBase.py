from bs4 import BeautifulSoup
import urllib2
import urllib
import cPickle

class  TorrentParserSettings:
	base_uri 	= ''
	site_name	= ''
	search_url	= ''

	def __repr__(self):
		return u"<TorrentParserSettings: base_uri:%s site_name:%s>" % (self.base_uri, self.site_name)


class Torrent:
	name 			= ''
	info_url 		= ''
	magnet_link		= ''
	torrent_url		= ''

	def get_magnet(self):
		return urllib.quote(self.magnet_link)

	def __repr__(self):
		return u"<Torrent: name:%s infoURL:%s magnet:%s>" % (self.name, self.info_url, self.magnet_link)

	def __str__(self):
		return self.__repr__()

class TorrentParserBase:

	def _constructurl(self, keywords):
		pass

	def _gethtmlpage(self, keywords):
		url = self._constructurl(keywords)
		print url
		u = urllib2.urlopen(url)
		contents = u.read()
		return contents

	def _parsepage(self, page):
		pass

	def findtorrents(self, keywords):
		htmlpage = self._gethtmlpage(keywords)
		return self._parsepage(htmlpage)
