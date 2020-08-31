import tkinter as tk

root = tk.Tk()
#root.geometry("350x350")




# Functions
def get_house_cost():
	return int(house_cost.get())

def get_down_payment():
	return int(down_payment.get())

def get_salary():
	return int(annual_salary.get())

def get_savings():
	return int(savings.get())

def get_savings_rate():
	return float(savings_rate.get())

def salary_increase():
	return float(semi_annual_raise.get())


def time_to_save():
	"""Main function for calculating months to save for down payment"""
	total_cost = get_house_cost()
	portion_down_payment = get_down_payment()
	salary = get_salary()
	current_savings = get_savings()
	monthly_salary = salary / 12
	portion_saved = get_savings_rate()
	raise_amount = salary_increase()

	months = 0
	while current_savings < portion_down_payment:
		if months != 0 and months % 6 == 0:
			salary += salary * raise_amount
		monthly_salary = salary / 12
		investment = round((current_savings * 0.04) / 12)
		monthly_saved = round(monthly_salary * portion_saved, 2)
		current_savings += monthly_saved
		current_savings = round(current_savings + investment, 2)
		months += 1

	months_to_payment = f"It will take {months} months to save {current_savings} for a down payment"
	months_to_save.delete("1.0", tk.END)
	months_to_save.insert(tk.INSERT, months_to_payment)
	return months_to_payment

#------------- Labels ---------------

title = tk.Label(root, text="Savings Calculator", font=24)
title.grid(row=0, columnspan=3)

app_description = tk.Text(root, wrap=tk.WORD, height=4, width=21)
app_description.insert(tk.INSERT, "An application to calculate savings for a house down payment")
app_description.grid(row=1, column = 0)

house_cost_label = tk.Label(root, text="Total cost of house")
house_cost_label.grid(row=2, column=0)

down_payment_label = tk.Label(root, text="Down payment")
down_payment_label.grid(row=4, column=0)

annual_salary_label = tk.Label(root, text="Annual Salary")
annual_salary_label.grid(row=6, column=0)

savings_label = tk.Label(root, text="Savings")
savings_label.grid(row=8, column=0)

savings_rate = tk.Label(root, text="Savings Rate")
savings_rate.grid(row=10, column=0)

semi_annual_raise = tk.Label(root, text="Semi Annual Raise")
semi_annual_raise.grid(row=12, column=0)



#-------------- Entry Fields ---------------

house_cost = tk.Entry(root)
house_cost.grid(row=3, column=0)

down_payment = tk.Entry(root)
down_payment.grid(row=5, column=0)

annual_salary = tk.Entry(root)
annual_salary.grid(row=7, column=0)

savings = tk.Entry(root)
savings.grid(row=9, column=0)

savings_rate = tk.Entry(root)
savings_rate.grid(row=11, column=0)

semi_annual_raise = tk.Entry(root)
semi_annual_raise.grid(row=13, column=0)


# Buttons
house = tk.Button(root, text="Enter", command=time_to_save)
house.grid(row=14, column=0)

# Display Fields
#months_saved = time_to_save()
months_to_save = tk.Text(root, height=4, width=20, wrap=tk.WORD)

months_to_save.insert(tk.INSERT, "months saved")
months_to_save.grid(row=15, column=0)






root.mainloop()
