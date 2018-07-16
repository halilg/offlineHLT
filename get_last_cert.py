#!/usr/bin/env python3

import re, os, sys
import urllib.request
from urllib.error import HTTPError, URLError

BASEURL='https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/' #don't forget the slash in the end

def fetchURL(url, timeout=5, encoding="utf-8"):
	try:
	    html = urllib.request.urlopen(url).read().decode(encoding)
	    return html
	except (HTTPError, URLError) as error:
	    print ('ERROR: Data of %s not retrieved because %s\nURL: %s', name, error, url)
	    return None

def get_new_json():
	index_html=fetchURL(BASEURL)
	cert_urls = re.findall(r'href=[\'"](Cert_[^\'" >]+_JSON.txt)', index_html)

	# Lets's simply take the last one
	lastcerturl = None if len(cert_urls)== 0 else cert_urls[-1]
	#print ("Latest golden json:", lasturl)
	if lastcerturl == None:
		print("Something went wrong, couldn't extract links..")
		sys.exit()

	# is the file already downloaded?
	if lastcerturl in os.listdir("."):
		sys.exit()

	# it's not, download it
	url = BASEURL+lastcerturl
	jsondata=fetchURL(url)
	with open(lastcerturl,"w") as f:
		f.write(jsondata)
	print("Retrieved", lastcerturl)
	return lastcerturl

if __name__ == "__main__":
	get_new_json()
