from geoip import open_database, geolite2
import csv
# with open_database('GeoLite2-City.mmdb') as db:
# 	# match = db.lookup_mine()
# 	match = geolite2.lookup('69.244.37.190')
# 	print 'My IP:', match
data = []
input_file = csv.DictReader(open("cleaned.csv"))
for row in input_file:
	data.append(row)

print data[1]	