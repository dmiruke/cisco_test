#!/usr/bin/env python

import os
import sys
import requests
import json
import re
from pprint import pprint
DEBUG = False

from requests.exceptions import HTTPError

# url = "https://api.macaddress.io/v1?apiKey=at_XVd1u1W5nVrzPHE15hvx6k5o7nSc0&output=json&search=" + macaddress

url = "https://api.macaddress.io/v1"
apiKey = "at_XVd1u1W5nVrzPHE15hvx6k5o7nSc0"

if (len(sys.argv) != 2):
   print ("Missing MAC address: %s <mac-address>" % (sys.argv[0]))
   sys.exit(-1)

macaddress = sys.argv[1]

if (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macaddress.lower())):
   url_str = url + '?apiKey=' + apiKey + '&output=json' + '&search=' + macaddress
else:
   print ("Mac address not in correct format")
   sys.exit(-1);

#print (json.dumps(response.text,  indent=4, sort_keys=True))

try:
  response = requests.get(url_str)
  if (response.status_code == 200):
     macData = json.loads(response.text)
     if DEBUG:
        pprint (macData)
     print ("Macaddress: %s, Company Name: %s" % (macData["macAddressDetails"]["searchTerm"], macData["vendorDetails"]["companyName"]))
except HTTPError as http_err:
  print ('HTTP error: {http_err}') 
except Exception as err:
  print ('Other error: {err}')
