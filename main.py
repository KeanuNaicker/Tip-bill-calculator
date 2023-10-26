currency = 'R' #currency symbol
totalbill = (input("What was the total bill amount?\n"))
split = (input("How many peope are splitting the bill?\n"))
percentage1 = (input("Would you like to give a 10, 15 or 20 % tip?\n"))

percentage2 = float("1."+percentage1)

payment = (float(totalbill)/ int(split)) * percentage2

finalamount = "{:.2f}".format(payment)

print(f'Each person should pay: {currency}{finalamount}')
