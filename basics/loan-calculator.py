# This program will calculate your current loan

# Loan details
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be, in dollars?\n"))
months = int(input("How many months do you want to see results for?\n"))

# Determine monthly rate
monthly_rate = apr/100/12

# Add interest
interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid

# Make payment
money_owed = money_owed - payment

# Show results
print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
print("Now I owe", money_owed)