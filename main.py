from flask import Flask
from flask import render_template
import transmissionrpc
import PirateproxyParser

web = Flask(__name__)

@web.route("/")
def home():
	tc = transmissionrpc.Client()
	tc.add_torrent('magnet:?xt=urn:btih:3b9e68d8a04a3c52da7483fcf84c863822b006a2&dn=How+I+Met+Your+Mother+S09E18+1080p+x264+Web-dl+5.1ch+AAC+%5BC7B%5D&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337')
		#'http://torcache.net/torrent/11667F9BEB5DBC551A41E7DFC33140DE4A5C161D.torrent?title=[katproxy.com]how.i.met.your.mother.s09e18.hdtv.x264.excellence.ettv')
		#'magnet:?xt=urn:btih:11667F9BEB5DBC551A41E7DFC33140DE4A5C161D&dn=how+i+met+your+mother+s09e18+hdtv+x264+excellence+ettv&tr=udp%3A%2F%2Ftracker.istole.it%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337')
	torrents =  tc.get_torrents()
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : str(torrents)
	}
	return render_template('layout.html', **templateData)

@web.route("/search")
def search():
	p = PirateproxyParser.PirateproxyParser()
	p.findtorrents(['How', 'I', 'Met', 'Your', 'Mother'])

if __name__ == '__main__':
	#web.run(host='0.0.0.0', port=8080, debug=True)
	search()