#! /usr/bin/python
#This script will download json data from https://data.cityofchicago.org and turn it into geojson data, suitable for Github.

import json
import urllib2

url = "https://data.cityofchicago.org/api/views/atzs-u7pv/rows.json?accessType=DOWNLOAD"

#download data and save complete original file to chi_farmers_market.json
d = json.load(urllib2.urlopen(url))
jdata = json.dumps(d, indent=4)
f = open('chi_farmers_market.json', 'w')
f.write(jdata)
f.close()

# take a subset of chi_farmers_market.json (key = "data") and save to a new file, farmers_data.json
rop = open('chi_farmers_market.json').read()
dget = json.loads(rop)
newdata = d["data"]
newarrayd = json.dumps(newdata, indent=4)
finalfile = open('farmers_data.json', 'w')
finalfile.write(newarrayd)
finalfile.close()

#manipulate file to create a geojson
g = open('farmers_data.json').read()
jg = json.loads(g)
a = dict(enumerate(jg))
