# 4.5 Detecting ranges using logical operators

# Logical AND, OR, and NOT (general)
# Logical Operator: treats operands as being True or False, and evaluates to True or False.

# Logical AND: True when both of its operands are True.
# Logical OR: True when at least one of its two operands are True.
# Logical NOT: True when its one operand is False, and vice versa.

# Detecting ranges with logical operators (general)

x = int(input("Enter number: "))

if (0 < x) and (x < 100):
    print("True")

else:
    print("False")

y = int(input("Enter number: "))

if (y < -4) or (y > 10):
    print("True")

else:
    print("False")

# Boolean and logical operators
# Boolean: refers to a value that is either True or False. (True and False must be capitalized). A programmer can assign a Boolean value by specifying True or False, or by evaluating an expression that yields a Boolean.

# Boolean AND: True when both operands are True.
# Boolean OR: True when at least one operand is True.
# Boolean NOT (opposite): True when the single operand is False (and False when operand is True).

user_channel = int(input("Enter Cable TV Channel Number: "))

if (user_channel >= 2) and (user_channel <= 499):
    channel_type = 'Standard Definition'

elif (user_channel >= 500) and (user_channel <= 599):
    channel_type = 'Paid Channel'

elif (user_channel >= 1002) and (user_channel <= 1499):
    channel_type = 'High Definition'

else:
    channel_type = 'Error'

print(f"Channel type: {channel_type}")

# Detecting ranges implicitly vs. explicitly
x = int(input("Enter any number: "))

if (x < 0):
    print("Negative")
elif (x >= 0) and (x <= 10):
    print("0...10")
elif (x >= 11) and (x <= 20):
    print("11...20")
else:
    print("21+")

# ^ This is explictly defined range ^

x = int(input("Enter any number: "))

if (x < 0):
    print("Negative")
elif (x <= 10):
    print("0...10")
elif (x <= 20):
    print("11...20")
else:
    print("21+")

# ^ This is implictly defined range ^

# 4.5.1: Detect number range

user_age = int(input())

if (user_age >= 18) and (user_age <= 25):
    print('Eligible')
else:
    print('Ineligible')
