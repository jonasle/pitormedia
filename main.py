from flask import Flask
from flask import render_template
import transmissionrpc
import PirateproxyParser

web = Flask(__name__)

@web.route("/")
def home():
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : ''
	}
	return render_template('layout.html', **templateData)

@web.route("/search/<keywords>")
def search(keywords):
	p = PirateproxyParser.PirateproxyParser()
	torrents = p.findtorrents(keywords)
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : torrents,
		'action' : {'search' : True}
	}
	#print torrents
	return render_template('layout.html', **templateData)

@web.route("/download/<uri>")
def download(uri):
	tc = transmissionrpc.Client()
	tc.add_torrent(uri)
	return render_template('layout.html', **templateData)

if __name__ == '__main__':
	web.run(host='0.0.0.0', port=8080, debug=True)
	#search('How I Met Your Mother')