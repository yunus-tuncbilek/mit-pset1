'''
house.py, Yunus Tuncbilek, September 2024.

This program is based on the first assignment in MIT OCW's intro python course
Computes how many months it takes the user to make a down payment for a house.
'''

# user inputs salary, savings rate, house cost data
# savings rate is stored as a decimal, not a percentage
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_rate = float(input("Enter the semi-­annual raise, as a decimal: "))

# annual rate of investment return
annual_return = 0.04

# number of months passed
month = 0

# how much the user will have saved by this month
current_savings = 0.0

# down payment needed
portion_down_payment = total_cost * 0.25

# checks if the user has saved enough
while current_savings < portion_down_payment:
    # indicate a new month has passed
    month += 1

    # the savings are increased by the monthly investment return rate
    current_savings += current_savings * annual_return / 12

    # every six months, the user gets a salary increase
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_rate

    # every month the user saves more money
    current_savings += annual_salary * portion_saved / 12

print("Number of months:", month)