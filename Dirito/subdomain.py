#!/bin/python3

import requests
import urllib3
import sys


# http://web.whatsapp.com
#       brute   domain   .com


try:
	host = str((sys.argv[1]))
	wordlist = str((sys.argv[2]))
	word_file = open(sys.argv[2],'rt')
	for i in word_file:
		eol = i.strip()
		url = i+'.'+host+'.com'
		r = requests.get(url)
		if r.status_code != 404:
			print(str(r.status_code)+" -> " +i.strip())
		else:
			continue 

except IndexError:
	print('Please provide some ip address')
except requests.exceptions.ConnectionError:
	print('Connection Error occured')
except requests.exceptions.Timeout:
	print('Exiting Timeout')
except KeyboardInterrupt:
	print('Exiting Now')
	
