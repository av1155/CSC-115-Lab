# 5.5 For loops

# For loop: Loops over each element in a container one at a time, assigning a variable with the next element that can then be used in the loop body. The container is usually a list, string, or tuple.

for names in ["Bill", "Nicole", "John"]:
    print(f"Hi {names}!")

print("Program Complete!\n")

# A for loop assigns the loop variable with a dictionary's keys.
channels = {
    "Netflix": 1,
    "HBO Max": 2,
    "Disney+": 3,
    "Hulu": 4,
}

for c in channels:
    print(f"{c} is on channel {channels[c]}")

print("Program Complete!\n")

# Using a for loop to access each character of a string.
my_str = ""
for character in "Take me to the moon":
    my_str += character + "_"
print(my_str)

print("Program Complete!\n")

# Examples of for loop

# Calculating shop revenue.
daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print(f'Weekly revenue: ${total:.2f}')
print(f'Daily average revenue: ${average:.2f}')

print("Program Complete!\n")

# Looping over a sequence in reverse.
names = [
    "Andrea",
    "Vanessa",
    "Paulina",
    "Arturo",
    "Tery"
]

for name in names:
    print(name, "|", end=" ")
print()

print("\nPrinting in reverse:")
for name in reversed(names):
    print(name, "|", end=" ")

print("\n")

# Assign num_neg with the number of below-freezing Celsius temperatures in the list.
temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]

num_neg = 0
for temp in temperatures:
    if temp < 0:
        num_neg += 1
print(num_neg)

print()

scores = [75, 77, 80, 85, 90, 95, 99]

for scr in reversed(scores):
    print(scr, end=" ")

print("\n")

word = 'Data'
for char in word:
    print(char, end=';')
print("\n")


cities = {
    'Nairobi': 958,
    'Paris': 5259,
    'Toronto': 309,
    'Montreal': 438,
    'Rome': 982,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)

# 5.5.2: For loop: Printing a list.
# NOTE: The following statement converts the input into a list container
stock_prices = input("Enter numbers to make into a list: ").split()

for price in stock_prices:
    print(f'${price}', end=" ")

print("\nProgram Complete!\n")

# 5.5.3: For loop: Printing a dictionary
contact_emails = {
    'Sue Reyn': 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input("Enter name: ")
new_email = input("Enter email: ")
contact_emails[new_contact] = new_email

for contact in contact_emails:
    print(f"{contact_emails[contact]} is {contact}")

print("Program Complete!\n")
