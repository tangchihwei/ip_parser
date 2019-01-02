from geoip import open_database, geolite2
import pycountry
from pycountry import countries
import csv

csv_data = []
unknown_data = []
country_dict = {}
region_dict = {}
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
					country_dict[match.country] =1
			else:
				unknown_data.append(a)

country_dict['GB'] = country_dict.pop('UK',None)

for c in country_dict:
	if c:
		print pycountry.countries.get(alpha_2=c).name + " : " + str(country_dict[c])

with open_database('GeoLite2-City.mmdb') as db:
	for a in csv_data:
		if a["REGION"]:
			r = a["REGION"]

			if r in region_dict:
				region_dict[cc] +=1
			else:
				region_dict[cc] = 1
		else:
			c = a["CONFIRM_IP"]
			match = geolite2.lookup(c)
			if match:
				a["REGION"] = match.subdivisions
				if match.subdivisions in region_dict:
					region_dict[match.country] +=1
				else:
					region_dict[match.country] =1
			else:
				unknown_data.append(a)



# for u in unknown_data:
# 	print u["Email Address"] + ": " + u["CONFIRM_IP"]
			
