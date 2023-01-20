wage = 20
hours = 8
weeks = 52
salary = wage * hours * weeks
print('Salary is:', salary)

hours = 4
weeks = 16
salary = 15

salary = wage * hours * weeks

print('New Salary is:', salary)

# With a hashtag you can make comments. A cool thing about Python is that it is very easy to understand for beginners. I have linked all of this to my GitHub repository and I am able to save my work on the cloud this way. Wage, hours, and weeks are all expressions because they yield a value. In this case, they yield the values, 20, 8, and 52. Then you can use the expression "salary" to get a result. In this new expression you can write down that wage * hours * weeks = the new salary. Print is used to print text and then show the result. In this case, I "print" the new salary.

print('Hello World')
# Print means output, text in between quotes is shown. a comma followed by an expression gives the text and the result of that expression. For example:
print('Hello World and this is my salary', salary)
# You can also use double quotes, specifically for text that contains single quotes, such as the word "don't". Ex:
print("don't print")
print(' ')
print('    **       **')
print('  *     *  *    *')
print(' *       *       *')
print('*                 *')
print(' *               *')
print('   *           *')
print('     *       *')
print('       *   *')
print('         *')

print('')

print('hello there.', end=' ')
print('My name is Andrea.')

wage = 100000
print('wage is', end=' ')
print(wage, end=' ')
print("it's lit")

print('Wage:', wage, 'Goodbye')

print('')

# You can use the charcater \n to print something in different lines. Example:

print('Welcome\nTo\nThe\nUniversity of Miami')

print('')

print('What was my first car?', end=' ')
first_car = input()
print('My first car was a', first_car)

print('')

my_string = '123'
my_int = int('123')

print(my_string)
print(my_int)

# Using int('1111') before an integer simply converts it into an integer. Then using something like my_var = int('1111') assigns the result to that variable. Which can then be used for calculations or other things. Example:

print('')

print('Enter wage:', end=' ')
wage = int(input())

new_wage = wage + 10
print('New wage:', new_wage)

# You can also use input() for calculations within the int statement. This will make the user input a number and then can be modified by the line of code.

print('')

# Input Prompt

hours = 40
weeks = 52
hourly_wage = int(input('Enter hourly wage: '))

print('Salary is', hourly_wage * hours * weeks)

print('')

human_years = int(input('Enter age of dog (in human years): '))
print()

dog_years = 7 * human_years

print(human_years, 'human years is about', end=' ')
print(dog_years, 'dog years.')

print('')

num1 = int(input('Write a number '))
num2 = int(input('Write a second number '))
print(num1 + num2)

print('')

num1 = int(input('Write a number '))
num2 = int(input('Write a second number '))
num3 = int(input('Divide by a number '))

print(num1 * num2 / num3)
