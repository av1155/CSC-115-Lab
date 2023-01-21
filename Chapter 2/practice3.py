import math
from pickletools import pyfloat


print('Variables and assignments')

print('3 2 1 Go!')

x = 5
y = 2
z = x * 10
a = z + y

print(a)

print()

y = 6
x = y + 2
y = 12

print(x, y)

''' The example above represents X as the sum of Y and 2; however, it shows Y as 12 because Y = 12 is the last variable in the array.'''

people_with_measles = int(input('How many people have measles? '))

x = people_with_measles * 20 * 20

print(people_with_measles, 'people with measles may cause',
      x, 'people to be infected per week')


nickel_count = int(input('How many nickels do you have? '))
dime_count = int(input('How many dimes do you have? '))

total_nickel = nickel_count * 5

total_dime = dime_count * 10

total_cents = total_nickel + total_dime

print('Your total amount of cents is:', total_cents)

dollar_amount = total_cents / 100

print('Your total amount of dollars is:', dollar_amount)

'''
Python 3 reserved keywords
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
'''

'''
2.4 Numeric types: Floating-point

There are floating-point numbers and floating-point literal.
A floating-point number is any number that has a decimal point appearing anywhere in the number. For example 98.6, or 0.00001, or -88.653.
A floating-point literal is written with the fractional part even if that fraction is 0, as in 1.0, 0.0, or 99.0.

Float is a data type for floating-point numbers.
'''

miles = float(input('Enter a distance in miles: '))

hours_to_fly = miles / 500
hours_to_drive = miles / 60

print(miles, 'miles would take')
print(hours_to_fly, 'hours to fly')
print(hours_to_drive, 'hours to drive')


print('2.0 to the power of 512 = ', 2.0 ** 512)

temperature_canada_fahrenheit = float(input('Temperature in Canada: '))
temperature_panama_fahrenheit = float(input('Temperature in Panama: '))

average_fahrenheit = (temperature_canada_fahrenheit +
                      temperature_panama_fahrenheit) / 2

print(f'{average_fahrenheit:.2f}', 'is the average fahrenheit temperature.')


print('Default output of Pi:', math.pi)
print('Pi reduced to 4 digits after the decimal:', end=' ')
print(f'{math.pi:.4f}')


# Below is the Challenge Activity of the section.

wall_area = float(input('How many square feet do you want to paint? '))

# Assign gallons_paint below

gallons_paint = wall_area / 350

print(f'{gallons_paint:.3}')
