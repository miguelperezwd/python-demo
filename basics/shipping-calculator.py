# This program will determine if you qualify for free shipping based on your order amount

orderAmount = int(input("What's your order total?\n"))

if orderAmount > 25:
    print("You get FREE shipping!")
else:
    # Add $15 of shipping charges
    newTotal = orderAmount + 15
    print("You don't qualify for free shipping, so we will charge $15 for shipping. Your new total is: " + str(newTotal))