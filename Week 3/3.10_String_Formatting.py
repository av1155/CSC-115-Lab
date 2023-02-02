# 3.10: String Formatting

# Formatted string literals (f-strings): Allows a programmer to create a string with placeholder expressions that are evaluated as the program executes.
# An F-string starts with an f charcater before the starting quote and uses curly braces { } to denote the placheolder expressions; these are also called a replacement field, because its value replaces the expression in the final output.

number = int(input("How many burritos? "))
cost = 5.33

print(f"{number} burritos at ${cost} each cost ${number * cost:.2f}")

print()

print(f"{number=}")
print(f"{cost=}")
print(f"{{2 ** 2}}")
print(f"{{{2 ** 2=}}}")

# Format Specifications: Allows the value's formatting i the string to be customized.
# This is the function of the :.2f after the value before it. For example: {2 * 2:.2f} makes it so the result is 4.00

# Presentation Type: format specification that presents a value depending on the type that follows the colon ( : ).

'''
Type	
Description	    
Example	    
Output

s	
String (default presentation type - can be omitted)	
name = 'Aiden'
print(f'{name:s}')
Aiden

d	
Decimal (integer values only)	
number = 4
print(f'{number:d}')
4

b	
Binary (integer values only)	
number = 4
print(f'{number:b}')
100

x, X	
Hexadecimal in lowercase (x) and uppercase (X) (integer values only)	
number = 31
print(f'{number:x}')
1f

e	
Exponent notation	
number = 44
print(f'{number:e}')
4.400000e+01

f	
Fixed-point notation (six places of precision)	
number = 4
print(f'{number:f}')
4.000000

.[precision]f	
Fixed-point notation (programmer-defined precision)	
number = 4
print(f'{number:.2f}')
4.00

0[precision]d	
Leading 0 notation	
number = 4
print(f'{number:03d}')
004

'''

print(f"{11:b}")

# 3.10.2: Printing an f-string
user_word = input()
user_number = int(input())

combine = user_word, user_number

print(*combine, sep=",")

# OR

user_word = input()
user_number = int(input())

print(f"{user_word},{user_number}")

print()

loan_rate = 0.08
borrowers_name = 'Ryder'

print(f"{borrowers_name}\'s loan rate is {loan_rate}")

# Use \' to add the symbol ' after the value.

"hi"
