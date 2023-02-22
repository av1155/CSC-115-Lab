# 5.2 While loops

# While loop: A construct that repeatedly executes an indented block of code (knows as the loop body) as long as the loop's expression is True. The loop always returns and runs it again until the expression results in False. Every "run" or "loop" is an iteration. Looping is also called "iterating".


curr_power = 2
user_char = 'y'

while user_char == 'y':
    print(curr_power)
    curr_power = curr_power * 2
    user_char = input()

print('Done')

'''
# Get character from user here
while user_char != 'n':
    # Do something
    # Get character from user here

NOTE: In this case, the loop runs zero times. Because user_char == 'n' the expression becomes false, and the loop body is never executed.

'''

################################################################


# While loop with a sentinel value

nose = "0"
user_value = "-"

while user_value != "q":
    print(f" {user_value} {user_value} ")  # Eyes
    print(f"  {nose}  ")  # Nose
    print(user_value * 5)
    print("\n")

    user_input = input(
        "Enter a character (use 'q' for quitting the program): ")
    user_value = user_input[0]

print("Goodbye.\n")

print("Program Complete")

################################################################

...
num = int(input("Enter a number: "))

# Print each digit
while num > 0:
    print(num % 10)
    num = num // 10

print("Program Complete")

################################################################

year_considered = 2020  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print(f'Ancestors in {year_considered}: {num_ancestors}')

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation

print("Program Complete")

################################################################

g = 4

while g <= 5:
    print(g)
    g += 1

################################################################

user_num = int(input("Enter a non-negative number: "))
while (user_num >= 0):
    print('Body')
    user_num = int(input())

print('Done.')

################################################################

user_num = int(input("Enter a number greater than 1: "))

while (user_num >= 1):
    user_num /= 2
    # Use an indented print to show every result in the terminal. If print is placed with no indentation at the end, it will just show the last result.
    print(user_num)
