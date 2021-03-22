# This program will sum all your expenses

expenses = [10, 5, 14.30, 20, 9, 15]
sum = 0

for x in expenses:
    sum = sum + x

print("You spent $", sum, " on lunch this week.", sep='')