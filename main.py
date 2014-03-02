from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import transmissionrpc
import PirateproxyParser

web = Flask(__name__)

@web.route("/")
def home():
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : '',
		'action' : {'search' : False}
	}
	templateData = build_template_data(templateData)
	return render_template('layout.html', **templateData)

@web.route("/search/", methods = ['POST', 'GET'])
def search(keywords = None):
	if(keywords is None):
		keywords = request.args.get('q', '')
	p = PirateproxyParser.PirateproxyParser()
	torrents = p.findtorrents(keywords)
	templateData = {
		'title' : 'Super-Awesome',
		'torrents' : torrents,
		'action' : {'search' : True}
	}
	#print torrents
	templateData = build_template_data(templateData)
	return render_template('layout.html', **templateData)

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
	return render_template('layout.html', **templateData)

def build_template_data(templateData):
	templateData['urls'] = {
		'search' 	: url_for('search'),
		'home'		: url_for('home')
	}
	return templateData

if __name__ == '__main__':
	web.run(host='0.0.0.0', port=8080, debug=True)
	#search('How I Met Your Mother')