div = 20 % 2
print(div)
div = 21 % 2
print(div)
div = 22 % 2
print(div)
div = 23 % 2
print(div)
div = 24 % 2
print(div)

print()

div = 20 % 3
print(div)
div = 21 % 3
print(div)
div = 22 % 3
print(div)
div = 23 % 3
print(div)
div = 24 % 3
print(div)

''' --------------------------------------------------------------------------------------------------------------------------------'''

change = int(input('How many cents do you have? '))

num_quarters = change // 25
change = change % 25
num_nickels = change // 5
change = change % 5
num_pennies = change // 1

total_coins = (num_quarters + num_nickels + num_pennies)
dollars = (change) / 100

print(
    "The total number of quarters is:", num_quarters, "the total number of nickels is:", num_nickels, "and the total number of pennies is:", num_pennies, "\nThe total number of dollars is:", f"{dollars:.2f}")

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''

change = int(input('Enter change: '))

num_quarters = change // 25
change = change % 25
num_nickels = change // 5
change = change % 5
num_pennies = change // 1

print(num_quarters)
print(num_nickels)
print(num_pennies)

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''

first_name = input("First Name: ")
middle_name = input("Middle Name: ")
last_name = input("Last Name: ")
middle_initial = middle_name[0]

full_name = first_name + " " + middle_name[0] + " " + last_name

print(full_name)

''' --------------------------------------------------------------------------------------------------------------------------------'''

myStudents = ["Andrea Venti", "Marc Rex", "John Smith"]

print(myStudents)
print(*myStudents)
