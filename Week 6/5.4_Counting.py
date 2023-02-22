# 5.4 Counting

# Counting while loop form.
# # Iterating N times using a loop variable
i = 1
while (i <= 5):
    # Loop body statements go here
    i = i + 1
print(i)

# A common error is to forget to include the loop variable update (e.g., i = i +1) at the end of the loop, causing an unintended infinite loop.

# While loop with loop variable that counts down.
i = 5
while i >= 1:
    # Loop body statements go here
    i = i - 1
print(i)

# Loop variable increased by 2 per iteration.
i = 0
while i <= 100:
    # Loop body statements go here
    i = i + 2
print(i)

########################################################################

'''Program that calculates savings and interest'''

initial_savings = 1000000
interest_rate = 0.0375

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(f' Savings at beginning of year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('Program Complete\n')

########################################################################

# By using i += 2 you can skip even integers.
# By using i += 5 you can use multiples of 5 to count.

# 0 to 10,000 by 500s (0, 500, 1000, ...)
i = 0
while i <= 10000:
    print(i, end=' ')
    i += 500
print("\n")

# -19 to 19 by 1s
i = -19
while i <= 19:
    print(i, end=' ')
    i += 1
print("\n")

# 10 to -10 by 1s
i = 10
while i >= -10:
    print(i, end=' ')
    i -= 1
print("\n")

# Multiples of 3 between 0 and 100
i = 0
while i <= 100:
    print(i, end=' ')
    i += 3
print("\n")

# Powers of 2 from 1 to 256 (1, 2, 4, 8, ...)

i = 1
while i <= 256:
    print(i, end=' ')
    i *= 2
print("\n")

########################################################################

# my_var += my_var/2

# is the same as

# my_var = my_var + my_var/2

########################################################################

num_printed = 0

num_stars = int(input("Enter a number: "))

while num_printed < num_stars:
    print('*', end=' ')
    num_printed += 1
print("\n")
