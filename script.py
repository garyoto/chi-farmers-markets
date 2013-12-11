#! /usr/bin/python

import json
import urllib2
import pickle

url = "https://data.cityofchicago.org/api/views/atzs-u7pv/rows.json?accessType=DOWNLOAD"

d = json.load(urllib2.urlopen(url))
jdata = json.dumps(d, indent=4)
f = open('chi_farmers_market.json', 'w')
f.write(jdata)
f.close()
