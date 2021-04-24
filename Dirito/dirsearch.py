#!/bin/python3

import sys
import requests
import urllib3
from urllib3.exceptions import HTTPError as BaseHTTPError





try: 
	C = str((sys.argv[1]))
	C2 = str((sys.argv[2]))
#	-> argv + i -> req
	f = open(sys.argv[2],"rt")
#	r = requests.get(sys.argv[1])
	for i in f:
		eol = i.strip()
		url = C+"/"+eol
		r = requests.get(url)
		if r.status_code != 404:
			print(str(r.status_code)+ "-> "+ i.strip())
		else:
			continue	
except IndexError:
	print("Please provide a URL and a wordlist")	
except requests.exceptions.ConnectionError:
    	print("Connection Error Occured")
except requests.exceptions.Timeout:
	print("Connection Timeout")
except KeyboardInterrupt:
	print("Exiting Now")

