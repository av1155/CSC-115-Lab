print("4.1: If-else branches (General)")

# Branch: Sequence of statements only executed under a certain condition.
# If: An if branch is a branch taken only if an expression is true.

hotel_rate = 160
user_age = int(input("Enter your age: "))

if user_age > 65:
    hotel_rate = hotel_rate - 30

print("Your rate: ", hotel_rate)
