# Removed total_cost from time_to_save function

# BUGS
	# If you enter the savings amount equal or greater than down payment, program
		# will bypass while loop and and try to reference a rate-based if statement
		# resulting in a "unboundlocalerror" because it references rate before rate
		# is assigned.  
	# Entering an amount for savings close to the down payment will also result
		# in an infinite loop, threshold is around ~600 of down payment 

class SavingsCalc:
	"""Class containing methods for calculating savings rates for house payments"""

	def __init__(self, total_cost, current_savings, annual_salary, semi_annual_raise):
		"""Initialize class attributes"""
		self.total_cost = total_cost
		self.current_savings = current_savings
		self.annual_salary = annual_salary
		self.semi_annual_raise = semi_annual_raise
		self.down_payment = int(self.total_cost * 0.25)


	def time_to_save(self, rate): # Removed salary and savings
		months = 0
		#self.down_payment = total_cost * 0.25
		savings = self.current_savings
		annual_salary = self.annual_salary
		while savings < self.down_payment:
			#print("Stuck in time to save")
			#print(f"{rate}: rate")
			if months != 0 and months % 6 == 0:
				annual_salary += (annual_salary * self.semi_annual_raise)
			monthly_salary = annual_salary / 12
			investment = round((savings * 0.04) / 12, 2)
			monthly_saved = round(monthly_salary * rate, 2)
			savings += monthly_saved
			savings = round(savings + investment, 2)
			if months >= 36: 
				break
			months += 1

		return savings, months


	def midpoint(self, start, end):
		mid = (end + start) / 2
		return mid


	def ideal_savings(self):
		start = 0
		end = 10000
		mid = self.midpoint(start, end)
		range_down_payment = range((self.down_payment - 100), (self.down_payment+ 101))
		counter = 0
		local_savings = self.current_savings
		while local_savings not in range_down_payment:
			mid = round(self.midpoint(start, end), 2)
			rate = round(mid / 10000, 4)
			local_savings = self.time_to_save(rate)[0] # Definetly something going on with self.current_savings and local_savings
			months = self.time_to_save(rate)[1]
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

#ideal_savings()
#test_savings = SavingsCalc(500_000, 0, 125_000, 0.07)
#test_savings.ideal_savings()

#second_test = SavingsCalc(1_000_000, 0, 150_000, 0.07)
#second_test.ideal_savings()

# PSET 1/B function
#portion_saved = .4411

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
	return months






#print(time_to_save(total_cost, portion_down_payment, annual_salary, current_savings))