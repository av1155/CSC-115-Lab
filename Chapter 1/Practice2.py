print('Current salary is:')
current_salary = int(input())
print('Current salary is:', current_salary)

print()

print('New salary is:')
new_salary = int(input())
print('New salary is:', new_salary)

# SyntaxError: The program contains invalid code that cannot be understood.
# IndentationError: The lines of the program are not properly indented.
# ValueError: An invalid value is used, which can occur if giving letters to int().
# NameError: The program tries to use a variable that does not exist.
# TypeError: An operation uses incorrect types, which can occur if adding an integer to a string.

current_salary = int(input('Enter your current salary '))

raise_percentage = 0.05

new_salary = current_salary + (current_salary * raise_percentage)

print('New salary', new_salary)

print('Hello World!', end=' ')

user_name = input()

print('Hello', user_name, 'and welcome to CS Online!')
