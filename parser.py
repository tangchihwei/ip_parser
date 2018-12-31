from geoip import open_database, geolite2
import csv
# with open_database('GeoLite2-City.mmdb') as db:
# 	match = geolite2.lookup('69.244.37.190')
	# print 'My IP:', match
csv_data = []
unknown_data = []
input_file = csv.DictReader(open("subs.csv"))
for row in input_file:
	csv_data.append(row)

with open_database('GeoLite2-City.mmdb') as db:
	for a in csv_data:
		if not a["CC"]:
		# print a["Email Address"]
			c = a["CONFIRM_IP"]
			# print type(c)
			match = geolite2.lookup(c)
			# print type(a["CONFIRM_IP"])
			if match:
				print match.country
			else:
				unknown_data.append(a)

for u in unknown_data:
	print u["Email Address"]
			
