numbers = 123456

rightMost2Digits = numbers % 100
print(rightMost2Digits)

div = 123456

leftMost2DigitsDiv = div // 10000

print(leftMost2DigitsDiv)

num_seconds = 4000

num_hours = num_seconds // 3600

num_seconds = num_seconds % 3600

num_minutes = num_seconds // 60

num_seconds = num_seconds % 60

print("Hours: ", num_hours)
print("Minutes: ", num_minutes)
print("Seconds: ", num_seconds)

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

print("Chapter 2 Review - Practice Coding about Modulo Operator")

change = int(input("Enter change:"))

numberOfQuarters = change // 25
change = change % 25

numberOfDimes = change // 10
change = change % 10

numberOfNickels = change // 5
change = change % 5

numbersOfPennies = change // 1

print("The number of quarter: ", numberOfQuarters)
print("The number of dime: ", numberOfDimes)
print("The number of nickel: ", numberOfNickels)
print("The number of penny: ", numbersOfPennies)

# Example of using String
firstName = "Hien"
middleName = "Minh"
lastName = "Nguyen"

middleInitial = middleName[0]

fullName = firstName + " " + middleName + " " + lastName

print(fullName)
print(middleInitial)

# Example of List
myStudent = ["Hien Nguyen", "Roger Williams", "Mirla Irias"]

print(myStudent)
print(*myStudent)
print(*myStudent, sep=" ;")

''' --------------------------------------------------------------------------------------------------------------------------------'''

myStudents = ["Andrea Venti", "Marc Rex", "John Smith"]

print(myStudents)  # Prints the list as is.
print(*myStudents)  # Prints the list without the brackets, commas and quotes.
print(*myStudents, sep=" ;"
      )  # Prints the list and adds a bracket in between words.

user_word = input()
user_number = int(input())

combine = user_word, user_number

print(*combine, sep=",")
