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
