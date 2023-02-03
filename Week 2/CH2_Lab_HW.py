''' 2.13 Lab: Divide input integers '''

user_num = int(input('Number 1: '))
div_num = int(input('Number 2: '))

result = user_num // div_num

result_2 = result // div_num

result_3 = result_2 // div_num

print('The integers when divided result in: ', result, result_2, result_3)

print('or')

user_num = int(input('Number 1: '))
div_num = int(input('Number 2: '))

user_num = user_num // div_num
print(user_num, end='')

user_num = user_num // div_num
print(user_num, end='')

user_num = user_num // div_num
print(user_num, end='')

print()

'''-----------------------------------------------------------------------------------------------------------------------------------'''''' 2.14 Lab: Driving costs '''

print()

# OUTPUT the gas cost for 25, 75, and 500 miles. INPUT gas_mileage, and gas_cost.

distance = 20
distance_2 = 75
distance_3 = 500
gas_mileage = float(input("What is the car's gas mileage? "))
gas_cost = float(input("How much does gas cost? "))

result1 = (distance / gas_mileage) * gas_cost
result2 = (distance_2 / gas_mileage) * gas_cost
result3 = (distance_3 / gas_mileage) * gas_cost

print(f'{result1:.2f} {result2:.2f} {result3:.2f}')

print()

'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 2.15 Lab: Expression for calories burned during workout '''

age = float(input('Age? '))
weight = float(input('Weight? '))
heart_rate = float(input('Average heart rate? '))
time = float(input('Time working out (in minutes)? '))

calories_burned = ((age * 0.2757) + (weight * 0.03295) +
                   (heart_rate * 1.0781) - 75.4991) * time / 8.368

print('Calories burned: 'f'{calories_burned:.2f}', 'calories')

print()

'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 2.18 Lab: Warm up: Variables, input, and type conversion '''

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space

user_int = int(input('Enter integer (32 - 126):\n'))

user_float = float(input('Enter float:\n'))

user_character = (input('Enter character:\n'))

user_string = (input('Enter string:\n'))

print(user_int, user_float, user_character, user_string)

print()

# FIXME (2): Output the four values in reverse

print(user_string, user_character, user_float, user_int)

# FIXME (3): Convert the integer to a character, and output that character

print(user_int, 'converted to a character is', chr(user_int))

print()

'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 2.19 Lab: Program: Cooking measurement converter'''

# FIXME (1): Finish reading other items into variables, then output the three ingredients

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

water_amount = float(input('Enter amount of water (in cups):\n'))

agave_amount = float(input('Enter amount of agave nectar (in cups):\n'))

servings_amount = float(input('How many servings does this make?\n'))

print()

print('Lemonade ingredients - yields', f'{servings_amount:.2f}', 'servings')
print(f'{lemon_juice_cups:.2f}', 'cup(s) lemon juice')
print(f'{water_amount:.2f}', 'cup(s) water')
print(f'{agave_amount:.2f}', 'cup(s) agave nectar')

print()

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

how_many = float(input('How many servings would you like to make?\n'))
print()

print('Lemonade ingredients - yields', f'{how_many:.2f}', 'servings')

lemon_servings_converted = how_many / 3
water_servings_converted = how_many / 0.375
agave_servings_converted = how_many / 2.4

print(f'{lemon_servings_converted:.2f}', 'cup(s) lemon juice')
print(f'{water_servings_converted:.2f}', 'cup(s) water')
print(f'{agave_servings_converted:.2f}', 'cup(s) agave nectar')

print()

# FIXME (3): Convert and output the ingredients from (2) to gallons

print('Lemonade ingredients - yields', f'{how_many:.2f}', 'servings')

lemon_cups_to_gallons = lemon_servings_converted / 16
print(f'{lemon_cups_to_gallons:.2f}', 'gallon(s) lemon juice')

water_cups_to_gallons = water_servings_converted / 16
print(f'{water_cups_to_gallons:.2f}', 'gallon(s) water')

agave_cups_to_gallons = agave_servings_converted / 16
print(f'{agave_cups_to_gallons:.2f}', 'gallon(s) agave nectar')
