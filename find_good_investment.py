#!/usr/bin/python
# Andrew main.py Version 1.0
# Created July 21, 2014
# Updated July 21, 2014

from urllib2 import urlopen
import time
import import_city_dic
import csv
import investment_analysis
import os; os.chdir('/Users/andrewkoo/Workspace/Real_Estate_Investment/')

def find_good_investment(parameters):
	
	threshold = 0.17 # Looking for ROI > threshold
	citydatabase = import_city_dic.import_city_dic()
	cities = citydatabase.keys()
	
	goodinvcsv = open('Files/good_investment_'+ time.strftime("%Y%m%d") + '.csv', 'wb')
	good_inv = csv.writer(goodinvcsv)
	
	columntitle = ["Property", "Property Type", "Price", "ROI", "URL"]
	good_inv.writerow(columntitle)
	
	for i in range(len(cities)):
		city = citydatabase[cities[i]]["Name"]
		
		if (os.path.isfile('Files/'+ city +'_for_sale_housing_data_'+ time.strftime("%Y%m%d") + '.csv') == True):
			citylistingcsv = open('Files/'+ city +'_for_sale_housing_data_'+ time.strftime("%Y%m%d") + '.csv', 'rU') 
			housing_list = csv.reader(citylistingcsv)
			for row in housing_list:
				if (row[0] != "Property Address" and row[4] != "N/A" and row[4] != "None" and row[7] != "None"):
					property_info = {}
					property_info["Name"] = row[0]
					property_info["Price"] = int(row[4][1:].replace(',',''))
					property_info["Property Appreciation Rate"] = 0.01 * float(row[13][:-1])
					property_info["URL"] = row[16]
				
					if (row[8] == "None"):
						property_info["House Value"] = property_info["Price"]
						property_info["Land Value"] = 0
					else:
						house_size = float(row[7])
						lot_size = float(row[8].replace(',',''))
						property_info["House Value"] = property_info["Price"] * house_size / (house_size + lot_size)
						property_info["Land Value"] = property_info["Price"] * lot_size / (house_size + lot_size)
				
					if (row[11] == "None"):
						property_info["HOA Monthly Fee"] = 0
					else:
						property_info["HOA Monthly Fee"] = int(row[11][1:].replace(',',''))
					
					ROI = investment_analysis.investment_analysis(parameters, property_info)
				
					if (ROI > threshold and row[2][:3] != "Mob"):
						good_inv.writerow([property_info["Name"], row[2], row[4], "{0:.1f}%".format(ROI * 100), property_info["URL"]])
	goodinvcsv.close()
	
if __name__ == '__main__':
	main()
