# 5.4 Counting

# # Iterating N times using a loop variable
# i = 1
# while (i <= N):
#     # Loop body statements go here
#     i = i + 1

# A common error is to forget to include the loop variable update (e.g., i = i +1) at the end of the loop, causing an unintended infinite loop.

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
