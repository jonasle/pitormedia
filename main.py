from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import transmissionrpc
import PirateproxyParser
import KatProxyParser

web = Flask(__name__)

@web.route("/")
def home():
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : '',
		'action' : {'search' : False}
	}
	return build_template(templateData)

@web.route("/search/", methods = ['POST', 'GET'])
def search(keywords = None):
	if(keywords is None):
		keywords = request.args.get('q', '')
	p = PirateproxyParser.PirateproxyParser()
	torrents = p.findtorrents(keywords)
	k = KatProxyParser.KatProxyParser()
	torrents += k.findtorrents(keywords)
	torrents = sorted(torrents, key=lambda torrent: torrent.seeders, reverse=True)
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : torrents,
		'q' : keywords,
		'action' : {'search' : True}
	}
	#print torrents
	return build_template(templateData)

@web.route("/download/<path:uri>")
def download(uri):
	tc = transmissionrpc.Client()
	ret = tc.add_torrent(uri)
	templateData = {
		'title' : 'Super-Awesome',
		'status' : ret,
		'action' : {
			'search' : False, 
			'status' : True}
	}
	return build_template(templateData)

def build_template(templateData):
	templateData['urls'] = {
		'search' 	: url_for('search'),
		'home'		: url_for('home')
	}
	if('q' not in templateData):
		templateData['q'] = ''
	return render_template('layout.html', **templateData)

if __name__ == '__main__':
	web.run(host='0.0.0.0', port=8080, debug=True)
	#search('How I Met Your Mother')