''' 4.15 LAB: Smallest number '''

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

min = x
if (y < min):
    min = y
if (z < min):
    min = z

print(min)

'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 4.18 LAB: Exact change '''

totalChange = int(input("Enter total amount of cents: "))
if (totalChange == 0):
    print("No change")

dollar = totalChange // 100
totalChange = totalChange % 100

quarter = totalChange // 25
totalChange = totalChange % 25

dime = totalChange // 10
totalChange = totalChange % 10

nickel = totalChange // 5
totalChange = total = totalChange % 5

penny = totalChange // 1


if (dollar == 1):
    print(dollar, "Dollar")
elif (dollar > 1):
    print(dollar, "Dollars")

if (quarter == 1):
    print(quarter, "Quarter")
elif (quarter > 1):
    print(quarter, "Quarters")

if (dime == 1):
    print(dime, "Dime")
elif (dime > 1):
    print(dime, "Dimes")

if (nickel == 1):
    print(nickel, "Nickel")
elif (nickel > 1):
    print(nickel, "Nickels")

if (penny == 1):
    print(penny, "Penny")
elif (penny > 1):
    print(penny, "Pennies")


'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 4.19 LAB: Leap year '''

year = int(input("Enter a year: "))

if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print(year, "- leap year")
else:
    print(year, "- not a leap year")

# If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4. It is not a leap year. For example: 1997 is not a leap year.
# If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. If a year is divisible by both 4 and 100, go to next step.
# If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both, then it is a leap year. So 2000 is a leap year.
