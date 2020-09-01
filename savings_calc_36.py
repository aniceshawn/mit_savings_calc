# Removed total_cost from time_to_save function

# I feel like I could make an object here and use these 5 values as attributes
total_cost = 500000
down_payment = int(total_cost * 0.25)
current_savings = 0
annual_salary = 32400
semi_annual_raise = 0.07


def time_to_save(annual_salary, current_savings, rate):
	months = 0
	down_payment = total_cost * 0.25
	while current_savings < down_payment:
		if months != 0 and months % 6 == 0:
			annual_salary += (annual_salary * semi_annual_raise)
		monthly_salary = annual_salary / 12
		investment = round((current_savings * 0.04) / 12, 2)
		monthly_saved = round(monthly_salary * rate, 2)
		current_savings += monthly_saved
		current_savings = round(current_savings + investment, 2)
		if months >= 36: 
			break
		months += 1
	return current_savings, months


def midpoint(start, end):
	mid = (end + start) / 2
	return mid

def ideal_savings():
	start = 0
	end = 10000
	mid = midpoint(start, end)
	range_down_payment = range((down_payment - 100), (down_payment+ 101))
	counter = 0
	local_savings = 0
	while current_savings not in range_down_payment:
		mid = round(midpoint(start, end), 2)
		rate = round(mid / 10000, 4)
		local_savings = time_to_save(annual_salary, current_savings, rate)[0]
		months = time_to_save(annual_salary, current_savings, rate)[1]
		counter += 1

		if int(local_savings) in range_down_payment:
			print(f"{months} months")
			break
		elif rate > .99:
			break
		elif local_savings > max(range_down_payment):
			end = mid 
		elif local_savings < min(range_down_payment):
			start = mid

	if rate >= .99:
		print("Not possible to save for a down payment in 36 months")
	else:
		print(local_savings)
		print(f"Search steps: {counter}")
		print(f"Savings rate: {rate}")
	#return

ideal_savings()

#down_payment =  int(total_cost * 0.25) # This is the ideal savings rate to get within 100 of down_payment
'''portion_down_payment = range((down_payment - 100), (down_payment + 101)) # This is the down_payment range
start = 0
end = 10000
#mid = midpoint(start, end)
counter = 0
savings = 0
while current_savings not in portion_down_payment: # While savings * mid not in target range
	mid = round(midpoint(start, end), 2)
	rate = round(mid / 10000, 4)
	savings = time_to_save(annual_salary, current_savings, rate)[0]
	months = time_to_save(annual_salary, current_savings, rate)[1]
	counter += 1
	#print(f"This is savings: {savings}")
	if int(savings) in portion_down_payment:
		print(f"{months} months")
		break
	elif savings > max(portion_down_payment):
		end = mid
		#print(f"{rate} Greater than")
	elif savings < min(portion_down_payment):
		start = mid
		#print(f"{rate} Less than")

print(savings)
print(f"Search steps: {counter}")
print(f"Savings rate: {rate}")'''







# PSET 1/B function
portion_saved = .4411

def time_to_save(total_cost, portion_down_payment, annual_salary, current_savings):
	months = 0
	while current_savings < portion_down_payment:
		if months != 0 and months % 6 == 0:
			annual_salary += (annual_salary * semi_annual_raise)
		monthly_salary = annual_salary / 12
		investment = round((current_savings * 0.04) / 12, 2)
		monthly_saved = round(monthly_salary * portion_saved, 2)
		current_savings += monthly_saved
		current_savings = round(current_savings + investment, 2)
		months += 1
	#print(f"It will take {months} months to save up enough for a down payment.")
	return months






#print(time_to_save(total_cost, portion_down_payment, annual_salary, current_savings))