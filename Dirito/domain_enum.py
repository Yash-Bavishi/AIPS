#!/bin/python3 

import sys
import requests
"""

Algo:
	Take User input -> (domain name) and (wordlist)
	Make the url such as -> http: wordlist.domain_name.com
	make a get request using http and Python requests module
	print status code and answer

"""

# Hardcoding

domain_name = "whatsapp"
wordlist = str((sys.argv[1]))
word_file = open(sys.argv[1],'rt')
for i in word_file:
	try:
		eol = i.strip()
		url = "http://"+eol+"."+domain_name+".com"
		r = requests.get(url)
		if r.status_code != 404:
			print(str(r.status_code) + "->" + url)
		else:
			continue
	except:
		pass
	
