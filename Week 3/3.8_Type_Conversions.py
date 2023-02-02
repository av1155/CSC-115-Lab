# 3.8: Type Conversions
num_births = int(input("How many births took place? "))

expected_males = 0.504 * num_births

print("The number of males born is:", expected_males)

# Type Conversion: This is a conversion of one type to another. Ex: Integer to float.
# Implicit Conversion: Type of conversion automatically made by the interpreter, usually between numeric types.

# integer-to-float conversion is straightforward: 25 becomes 25.0.    float-to-integer conversion just drops the fraction: 4.9 becomes 4.

''' When an integer is multiplied by a float, the integer then results in a float number. '''

# This multiplication turned the integer to a decimal result.
print(str(10 * 29.34))

print()

input_text = input("Enter a number: ")
input_float = float(input_text)
float_to_input = int(input_float)

print("The original input was converted to a decimal number:", input_float)
print("This number was converted from float to integer:", float_to_input)
# Conversions from input, to float, to integer.

print()

# Make the list of integers provide an average in the print.
avg_owls = 0.0

num_owls_zooA = int(input())
num_owls_zooB = int(input())
num_owls_zooC = int(input())


avg_owls = [num_owls_zooA, num_owls_zooB, num_owls_zooC]

avg_owls = (sum(avg_owls) / len(avg_owls))


print(f'Average owls per zoo: {int(avg_owls)}')

print()

# Make the normal input add them together as integers.
total_owls = 0

num_owls_A = input()
num_owls_B = input()

total_owls = int(num_owls_A) + int(num_owls_B)

print(f'Number of owls: {total_owls}')
