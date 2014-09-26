#!/usr/bin/python
# Andrew import_sold_housing_data.py Version 1.0
# Created July 23, 2014
# Updated July 23, 2014

from bs4 import BeautifulSoup
import numpy

def get_num_pages(soup):
	
	pagenumlist = soup.find("ul","pagination-2012 zbti")
	numlist = [a.string for a in pagenumlist.findAll("a", "")]
	numpages = int(numlist[-2])
	
	return numpages

def get_basic_info(property_soup):
	
	property_info = {}
	
	property_info["Property Address"] = "None"
	property_info["Zip Code"] = "None"
	property_info["Property Type"] = "None"
	property_info["Sold Price"] = "None"
	property_info["Sold Date"] = "None"
	property_info["Bed"] = "None"
	property_info["Bath"] = "None"
	property_info["House Size"] = "None"
	property_info["Lot Size"] = "None"
	property_info["Year Built"] = "None"
	property_info["Price / Sqft"] = "None"
	property_info["HOA Fee"] = "None"
	property_info["Recent Year Property Tax"] = "None"
	property_info["Neighborhood Appreciation Rate"] = "None"
	property_info["City Appreciation Rate"] = "None"
	property_info["Avg. School Rating"] = "None"
	
	prop_addr_h1 = property_soup.find("h1", "prop-addr")
	if (prop_addr_h1 is not None):
		property_info["Property Address"] = prop_addr_h1.text.encode('utf-8')
		property_info["Zip Code"] = property_info["Property Address"][-5:]
		print property_info["Property Address"]
	
	prop_summary = property_soup.find("div", "prop-mod prop-summary")
	if (prop_summary is not None):
		property_summary = prop_summary.text.split("\n")
		if (len(property_summary) >= 5):
			property_summary = property_summary[3].encode('utf-8').split(" ")
			if (property_summary[-6] != ""):
				property_info["Bed"] = property_summary[-6]
				if (property_summary[-4] != ""):
					property_info["Bath"] = property_summary[-4]
			elif (property_summary[-6] == "" and property_summary[-4] != ""):
				property_info["Bed"] = property_summary[-4]
			property_info["House Size"] = property_summary[-2].replace(',','')
	
	recently_sold_div = property_soup.find("div", "recently-sold")
	if (recently_sold_div is not None):
		summary_row = [span.string for span in recently_sold_div.findAll("span", "")]
		property_info["Sold Price"] = summary_row[1].encode('utf-8')
		property_info["Sold Date"] = summary_row[2].encode('utf-8')
	
	facts_div = property_soup.find("div", "prop-description-wrapper")
	fact_bullets = [div.string.encode('utf-8') for div in facts_div.findAll("div", "fact-bullet")]
	for i in range(len(fact_bullets)):
		item = fact_bullets[i]
		if (len(item) >= 5):
			code = item[:5]
			str_length = len(item)
			if (code == "Lot: "):
				property_info["Lot Size"] = item.split(" ")[1]
			elif (code == "HOA F"):
				property_info["HOA Fee"] = item.split(" ")[-1]
			elif (code == "Built"):
				property_info["Year Built"] = item.split(" ")[-1]
			elif (code == "Price"):
				property_info["Price / Sqft"] = item.split(" ")[-1]
			elif (code == "Townh" or code == "Condo" or code == "Singl" or code == "Multi" or code == "Mobil" or code == "Apart"):
				property_info["Property Type"] = item
	
	nh_div = property_soup.find("div", "za-track-event forecast-text notranslate")
	if (nh_div is not None):
		nh_description = nh_div.text.encode('utf-8').split(" ")
		percentage_words = []	
		for i in range(len(nh_description)):
			if (nh_description[i] != ""):
				if (nh_description[i][-1] == "%"):
					percentage_words.append(nh_description[i])
		property_info["Neighborhood Appreciation Rate"] = percentage_words[0]
		property_info["City Appreciation Rate"] = percentage_words[1]
	
	expense_div = property_soup.find("span", "vendor-cost")
	if (expense_div is not None):
		property_info["Recent Year Property Tax"] =  expense_div.text.encode('utf-8')[:-3]
	
	school_list = [span.string.encode('utf-8') for span in property_soup.findAll("span", "gs-rating-number")]
	if (school_list is not None):
		school_rating = []
		for i in range(len(school_list)):
			if (school_list[i].isdigit()):
				school_rating.append(float(school_list[i]))
		schooo_mean_rating = numpy.mean(school_rating)
		property_info["Avg. School Rating"] = ("%.1f" % schooo_mean_rating)
	
	return property_info
