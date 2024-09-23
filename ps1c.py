'''
house.py, Yunus Tuncbilek, September 2024.

This program is based on the first pset in MIT OCW's intro python course.
The following is my solution, produced when teaching python to highschoolers.
It computes how many months it takes the user to make a down payment for a house.
'''

# Calculates the number of months it would take to save the down payment 
# Returns a tuple with the number of months and the amount that would be saved 
#   by the end of the last month.
# The number of months is returned as -1 if it would be greater than 36. This 
#   is a design choice for the MIT assignment.
def monthsToDownPayment(annual_salary, portion_saved, total_cost, \
                           semi_annual_rate):
    # annual rate of investment return
    annual_return = 0.04

    # number of months passed
    month = 0

    # how much the user will have saved by this month
    current_savings = 0.0

    # down payment needed
    portion_down_payment = total_cost * 0.25

    # checks if the user has saved enough
    # every iteration of the while loop is a new month
    while current_savings < portion_down_payment:
        # indicate a new month has passed
        month += 1

        # if it's not possible to finish in 36 months, 
        # return (-1, current savings) to send a signal 
        if month > 36:
            return (-1, current_savings)

        # the savings are increased by the monthly investment return rate
        current_savings += current_savings * annual_return / 12

        # every six months, the user gets a salary increase
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_rate

        # every month the user saves more money
        current_savings += annual_salary * portion_saved / 12

    return (month, current_savings)

annual_salary = float(input("Enter the starting salary: "))

# Identify three saving rates, low, high, current to track bisection search
# this rate represents the highest confirmed-unsuccessful rate
low_savings_rate = 0
# this rate represents the lowest confirmed-successful rate
# Note: initially we do not know if 100 percent saving would be successful.
#   This is checked below.
high_savings_rate = 10000 
current_savings_rate = (low_savings_rate + high_savings_rate) / 2

# Check if it is at all possible to save for the house in 36 months 
month, savings = monthsToDownPayment(annual_salary, high_savings_rate/10000\
                                     , 10**6, 0.07)
if month == -1:
    print("It is not possible to pay the down payment in three years.")
    exit()

# number of bisection search iterations
steps = 0

while True:
    # We have found the point separating the successful and unsuccessful
    if high_savings_rate == low_savings_rate + 1:
        # high_savings_rate would represent the lowest successful rate
        print("Best savings rate:", high_savings_rate)
        print("Steps in bisection search:", steps)
        # print(high_savings_rate, savings)
        break

    # perform the calculation for the current savings rate
    month, savings = \
        monthsToDownPayment(annual_salary, current_savings_rate/10000, 10**6, 0.07)

    # print(steps, current_savings_rate, month, savings, low_savings_rate, high_savings_rate)

    # record the new step by increasing the steps variable
    steps += 1

    # if the current savings rate is not enough for 36 months
    if month == -1:
        # continue bisection search on the right interval
        low_savings_rate = current_savings_rate
        current_savings_rate = int((current_savings_rate + high_savings_rate) / 2)
        continue
    
    # if the current savings rate is enough, continue search on the left interval
    high_savings_rate = current_savings_rate
    current_savings_rate = int((current_savings_rate + low_savings_rate) / 2)