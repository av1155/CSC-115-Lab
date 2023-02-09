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
