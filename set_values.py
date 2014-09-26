#!/usr/bin/python
# Andrew set_values.py Version 1.0
# Created July 21, 2014
# Updated July 21, 2014

def set_values():
    
   	values = {}
   
   	# Initial Investment
   	values["Down Payment %"] = 0.25
   	values["Closing Cost %"] = 0.01
   
   	# Mortgage
   	values["Mortgage Term"] = 30 # Years
   	values["Interest Rate"] = 0.045
   
   	# Expense
   	values["Property Tax Rate"] = 0.0125
   	values["Insurance Rate"] = 0.002
   
   	# Taxes
   	values["Tax Bracket"] = 0.30
   	values["Long Term Capital Gain Rate"] = 0.15
   	values["State Tax Rate"] = 0.103
   
   	# Selling the Property
   	values["Property Holding Term"] = 5 # Years
   	values["Agent Fee Rate"] = 0.05
   
   	# Other Calcuations
   	values["Mortgage Amount %"] = 1 - values["Down Payment %"]
   
   	if (values["Property Holding Term"] >= 2):
   		values["Federal Tax Rate"] = 0
   	else:
		values["Federal Tax Rate"] = values["Long Term Capital Gain Rate"]
	
	return values