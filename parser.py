from geoip import open_database, geolite2
import pycountry
from pycountry import countries
import csv

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
			c = a["CONFIRM_IP"]
			match = geolite2.lookup(c)
			if match:
				a["CC"] = match.country
				if match.country in country_dict:
					country_dict[match.country] +=1
			else:
				unknown_data.append(a)

for c in country_dict:
	if c == "UK":
		country_dict['GB'] = country_dict.pop(c)
		c = 'GB'
	else:
		print pycountry.countries.get(alpha_2=c).name + " : " + str(country_dict[c])

# for u in unknown_data:
# 	print u["Email Address"] + ": " + u["CONFIRM_IP"]
			
