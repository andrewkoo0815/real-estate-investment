#!/usr/bin/python
# Andrew investment_analysis.py Version 1.0
# Created July 21, 2014
# Updated July 21, 2014

import numpy
import math
import os; os.chdir('/Users/andrewkoo/Workspace/Real_Estate_Investment/')


def investment_analysis(parameters, house_info):
	
	# Initial Investment
	total_price = house_info["House Value"] + house_info["Land Value"]
	down_payment = total_price * parameters["Down Payment %"]
	closing_costs = total_price * parameters["Closing Cost %"]
	
	initial_inv = down_payment + closing_costs
	
	# Mortgage
	total_mortgage = total_price * parameters["Mortgage Amount %"]
	term = parameters["Mortgage Term"]
	interest_rate = parameters["Interest Rate"]
	monthly_payment = abs(numpy.pmt(interest_rate / 12, term * 12, total_mortgage))
	
	annual_payment = monthly_payment * 12
	
	# Expense
	property_tax = total_price * parameters["Property Tax Rate"]
	property_insurance = total_price * parameters["Insurance Rate"]
	hoa_fee = 12 * house_info["HOA Monthly Fee"]
	
	annual_expense = property_tax + property_insurance + hoa_fee
	
	# Tax Savings
	holding_period = parameters["Property Holding Term"]
	depreciation = house_info["House Value"] / 27.5
	deductions = []
	
	principal_payment = 0
	for i in range(holding_period):
		interest_deduction = 0
		for j in range(1, 13):
			interest_deduction = interest_deduction + abs(numpy.ipmt(interest_rate / 12, i * 12 + j, term * 12, total_mortgage))
			principal_payment = principal_payment + abs(numpy.ppmt(interest_rate / 12, i * 12 + j, term * 12, total_mortgage))
		deductions.append(annual_expense + depreciation + interest_deduction)
	
	tax_savings = [x * parameters["Tax Bracket"] for x in deductions]
	
	# Selling the Property
	sale_price = total_price * math.pow((1 + house_info["Property Appreciation Rate"]), holding_period)
	profit = sale_price * (1 - parameters["Agent Fee Rate"]) - total_price
	federal_tax = profit * parameters["Federal Tax Rate"]
	state_tax = profit * parameters["State Tax Rate"]
	mortgage_payoff = total_mortgage - principal_payment
	
	# Cash Flow
	cash_flow = []
	for i in range(holding_period):
		cash_flow.append(tax_savings[i] - annual_expense - annual_payment)
	cash_flow[-1] = cash_flow[-1] + total_price + profit - federal_tax - state_tax - mortgage_payoff
	cash_flow = [-1 * initial_inv] + cash_flow

	ROI = numpy.irr(cash_flow)
	
	return ROI
