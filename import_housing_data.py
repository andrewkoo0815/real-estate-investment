#!/usr/bin/python
# Andrew import_sold_housing_data.py Version 1.0
# Created July 23, 2014
# Updated July 23, 2014

from bs4 import BeautifulSoup
from urllib2 import urlopen
import get_specific_data
import import_city_dic
import requests
import time
import csv
import os; os.chdir('/Users/andrewkoo/Workspace/Real_Estate_Investment/')

BASE_URL = "http://www.zillow.com"
SIGNIN_URL="https://www.zillow.com/user/account/services/Login.htm"


def make_soup(url):
    
    if (url[:45] == "http://www.zillow.com/homedetail/AuthRequired"):
    	payload = {'email': 'XXXYYYZZZ@gmail.com', 'password': 'ABCDEFG123'}
    	with requests.Session() as s:
    		r = s.post(SIGNIN_URL, data=payload)
    		r = s.get(url)
    	html = urlopen(r.url).read()
    else:
    	html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")
    
    
def gen_housing_url_list(url, city):
	
	soup = make_soup(url)
	numpages = get_specific_data.get_num_pages(soup)
	urllist = []
	statuslist = []
	pricelist = []
	
	for i in range(1, numpages + 1):
		pageurl = url + str(i) + "_p/"
		pagesoup = make_soup(pageurl)
		popbubble = pagesoup.find("div", "pop-bubble")
		pageurllist  = [BASE_URL + dt.a["href"] for dt in popbubble.findAll("dt", "property-address")]
		pagestatuslist = [str(dl.dt.strong.string) for dl in popbubble.findAll("dl", "property-info-sheet pier-2")]
		pagepricelist = [str(dt.strong.string) for dt in popbubble.findAll("dt", "price-large")]
		urllist = urllist + pageurllist
		statuslist = statuslist + pagestatuslist
		pricelist = pricelist + pagepricelist
	return urllist, statuslist, pricelist


def write_sold_housing_data(url, city):
	[urllist, statuslist, pricelist] = gen_housing_url_list(url, city)
	
	soldhousingdatacsv = open('Files/'+ city +'_sold_housing_data_'+ time.strftime("%Y%m%d") + '.csv', 'wb')
	sold_housing_data = csv.writer(soldhousingdatacsv)
	
	columntitle = []
	columntitle.append("Property Address")
	columntitle.append("Zip Code")
	columntitle.append("Property Type")
	columntitle.append("Sold Price")
	columntitle.append("Sold Date")
	columntitle.append("Bed")
	columntitle.append("Bath")
	columntitle.append("House Size")
	columntitle.append("Lot Size")
	columntitle.append("Year Built")
	columntitle.append("Price / Sqft")
	columntitle.append("HOA Fee")
	columntitle.append("Recent Year Property Tax")
	columntitle.append("Neighborhood Appreciation Rate")
	columntitle.append("City Appreciation Rate")
	columntitle.append("Avg. School Rating")
	columntitle.append("URL")
	
	sold_housing_data.writerow(columntitle)
	
	for i in range(len(urllist)):
		property_url = urllist[i]
		property_soup = make_soup(property_url)
		
		property_data =[]
		property_info = get_specific_data.get_basic_info(property_soup)
		
		property_data.append(property_info["Property Address"])
		property_data.append(property_info["Zip Code"])
		property_data.append(property_info["Property Type"])
		property_data.append(property_info["Sold Price"])
		property_data.append(property_info["Sold Date"])
		property_data.append(property_info["Bed"])
		property_data.append(property_info["Bath"])
		property_data.append(property_info["House Size"])
		property_data.append(property_info["Lot Size"])
		property_data.append(property_info["Year Built"])
		property_data.append(property_info["Price / Sqft"])
		property_data.append(property_info["HOA Fee"])
		property_data.append(property_info["Recent Year Property Tax"])
		property_data.append(property_info["Neighborhood Appreciation Rate"])
		property_data.append(property_info["City Appreciation Rate"])
		property_data.append(property_info["Avg. School Rating"])
		property_data.append(property_url)
		
		sold_housing_data.writerow(property_data)
	
	soldhousingdatacsv.close()
	

def write_for_sale_housing_data(url, city):
	[urllist, statuslist, pricelist] = gen_housing_url_list(url, city)
	
	forsalehousingdatacsv = open('Files/'+ city +'_for_sale_housing_data_'+ time.strftime("%Y%m%d") + '.csv', 'wb')
	for_sale_housing_data = csv.writer(forsalehousingdatacsv)
	
	columntitle = []
	columntitle.append("Property Address")
	columntitle.append("Zip Code")
	columntitle.append("Property Type")
	columntitle.append("Sale Type")
	columntitle.append("Offer Price")
	columntitle.append("Bed")
	columntitle.append("Bath")
	columntitle.append("House Size")
	columntitle.append("Lot Size")
	columntitle.append("Year Built")
	columntitle.append("Price / Sqft")
	columntitle.append("HOA Fee")
	columntitle.append("Recent Year Property Tax")
	columntitle.append("Neighborhood Appreciation Rate")
	columntitle.append("City Appreciation Rate")
	columntitle.append("Avg. School Rating")
	columntitle.append("URL")
	
	for_sale_housing_data.writerow(columntitle)
	
	for i in range(len(urllist)):
		property_url = urllist[i]
		property_sale_type = statuslist[i]
		if (property_sale_type == "None"):
			property_sale_type = "Make Me Move"
		property_offer_price = pricelist[i]
		property_soup = make_soup(property_url)
		
		property_data =[]
		property_info = get_specific_data.get_basic_info(property_soup)
		
		property_data.append(property_info["Property Address"])
		property_data.append(property_info["Zip Code"])
		property_data.append(property_info["Property Type"])
		property_data.append(property_sale_type)
		property_data.append(property_offer_price)
		property_data.append(property_info["Bed"])
		property_data.append(property_info["Bath"])
		property_data.append(property_info["House Size"])
		property_data.append(property_info["Lot Size"])
		property_data.append(property_info["Year Built"])
		property_data.append(property_info["Price / Sqft"])
		property_data.append(property_info["HOA Fee"])
		property_data.append(property_info["Recent Year Property Tax"])
		property_data.append(property_info["Neighborhood Appreciation Rate"])
		property_data.append(property_info["City Appreciation Rate"])
		property_data.append(property_info["Avg. School Rating"])
		property_data.append(property_url)
		
		for_sale_housing_data.writerow(property_data)
	
	forsalehousingdatacsv.close()


def import_housing_data():
    
    sold_url = "http://www.zillow.com/homes/recently_sold/"
    for_sale_url = "http://www.zillow.com/homes/for_sale/"
    
    # Import City Information
    citylist = import_city_dic.import_city_dic()
    cities = citylist.keys()
    # for i in range(len(cities)):
    for i in range(1):
		city = cities[i]
		city = "Sunnyvale"
		city_name = citylist[city]["Name"]
		write_sold_housing_data(sold_url + citylist[city]["location-URL"], city_name)
		write_for_sale_housing_data(for_sale_url + citylist[city]["location-URL"], city_name)
