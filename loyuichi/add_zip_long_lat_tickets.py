from geopy.geocoders import GoogleV3

import json
import dml
import prov.model
import datetime
import uuid

# Set up the database connection.
client = dml.pymongo.MongoClient()
repo = client.repo
repo.authenticate('loyuichi', 'loyuichi')

#geolocator = Nominatim()
geolocator = GoogleV3()

addresses = {}
for ticket in repo['loyuichi.towed'].find({"zip": {'$exists': True}, '$where': "this.zip.length == 4"}):
	try:
		zipcode = "0" + ticket['zip']
		res = repo['loyuichi.towed'].update({'_id': ticket['_id']}, {'$set': {'zip': zipcode}})
		print(res)
	except:
		pass

for meter in repo['loyuichi.meters'].find({"zip": {'$exists': True}, '$where': "this.zip.length == 4"}):
	try:
		zipcode = "0" + meter['zip']
		res = repo['loyuichi.meters'].update({'_id': meter['_id']}, {'$set': {'zip': zipcode}})
		print(res)
	except:
		pass
