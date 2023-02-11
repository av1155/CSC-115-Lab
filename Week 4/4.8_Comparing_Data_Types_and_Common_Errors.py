# 4.8 Comparing data types and common errors

# Comparing integers, strings, and floating-point types

""" 
- Integers can be compared.
- Strings can be compared.
- Floats cannot be compared.
"""

x = [1, 5, 2]
y = [1, 2, 3]

if (x < y):
    print("True")
else:
    print("False")

print()

user_num = int(input())

if user_num <= 2:
    print('Num is less or equal to two')
else:
    print('Num is greater than two')
