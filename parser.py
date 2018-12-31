from geoip import open_database, geolite2
import csv
# with open_database('GeoLite2-City.mmdb') as db:
# 	match = geolite2.lookup('69.244.37.190')
	# print 'My IP:', match
csv_data = []
unknown_data = []
country_dict = {}
input_file = csv.DictReader(open("subs.csv"))
for row in input_file:
	csv_data.append(row)

with open_database('GeoLite2-City.mmdb') as db:
	for a in csv_data:
		if a["CC"]:
			cc = a["CC"]
			if cc in country_dict:
				country_dict[cc] +=1
			else:
				country_dict[cc] = 1
		else:
		# print a["Email Address"]
			c = a["CONFIRM_IP"]
			# print type(c)
			match = geolite2.lookup(c)
			# print type(a["CONFIRM_IP"])
			if match:
				# print match.country
				a["CC"] = match.country
				if match.country in country_dict:
					country_dict[match.country] +=1
			else:
				unknown_data.append(a)

print country_dict

for u in unknown_data:
	print u["Email Address"] + ": " + u["CONFIRM_IP"]
			
