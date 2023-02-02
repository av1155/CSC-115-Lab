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
