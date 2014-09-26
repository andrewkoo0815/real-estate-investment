#!/usr/bin/python
# Andrew main.py Version 1.0
# Created July 21, 2014
# Updated July 21, 2014

import import_housing_data
import set_values
import find_good_investment
import os; os.chdir('/Users/andrewkoo/Workspace/Real_Estate_Investment/')


def main():
	
	# Import Listings
	import_housing_data.import_housing_data()
	
	# Import Parameters
	# parameters = set_values.set_values()
	
	# Find Good Investment
	# find_good_investment.find_good_investment(parameters)
	
if __name__ == '__main__':
	main()
