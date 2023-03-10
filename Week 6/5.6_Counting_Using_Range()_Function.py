# 5.6 Counting using the range() function

# NOTE While loops: Used for counting a specific number of iterations.
# NOTE For loops: Used to iterate over all elements of a container.
# NOTE range(): Allows counting in for loops as well.

# range() generates a sequence of integers between a starting integer that is included in the range, an ending integer that is not included in the range, and an integer step value. The sequence is generated by starting at the start integer and incrementing by the step value until the ending integer is reached or surpassed.

'''
range(Y) generates a sequence of all non-negative integers less than Y.
Ex: range(3) creates the sequence 0, 1, 2.

range(X, Y) generates a sequence of all integers >= X and < Y.
Ex: range(-7, -3) creates the sequence -7, -6, -5, -4.

range(X, Y, Z), where Z is positive, generates a sequence of all integers >= X and < Y, incrementing by Z.
Ex: range(0, 50, 10) creates the sequence 0, 10, 20, 30, 40.

range(X, Y, Z), where Z is negative, generates a sequence of all integers <= X and > Y, incrementing by Z.
Ex: range(3, -1, -1) creates the sequence 3, 2, 1, 0.

'''

# Ex:
# range(0, 5, 2)
# it counts every 2nd integer from 0 to 4.

# range(5(from), 0(to), -1(counting number))
# it counts every 1 integer from 5 to 1.

# Calculating yearly savings every three years.
'''Program that calculates savings and interest every three years'''

initial_savings = 10000
interest_rate = 0.0375
print()

savings = initial_savings
for i in range(0, 100, 3):
    print(f' Savings in year {i}: ${savings:.2f}')
    savings = savings + (savings*(interest_rate * 3))

print('\n')
