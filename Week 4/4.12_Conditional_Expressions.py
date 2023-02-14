# 4.12 Conditional expressions
# A conditional expression has the following form:

# expr_when_true "if" condition "else" expr_when_false

# Condition in the middle is evaluated first. If true, then expr_when_true is evaluated, if false, then expr_when_false is evaluated.

# Sometimes referred to as a ternary operation (because it has three conditions)

# These are actually denounced by Python programmers because they are difficult to read and comprehend. Left to right syntax is preferred.

user_val = int(input())

cond_str = "negative" if user_val < 0 else "nonnegative"

print(f'{user_val} is {cond_str}')

print()

num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if update_direction == 3 else num_users - 1

print(f'New value is: {num_users}')
