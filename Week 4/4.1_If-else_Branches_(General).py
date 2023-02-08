print("4.1: If-else branches (General)")

# Branch: Sequence of statements only executed under a certain condition.
# If: An if branch is a branch taken only if an expression is true.

hotel_rate = 160
user_age = int(input("Enter your age: "))

if user_age > 65:
    hotel_rate = hotel_rate - 30

print("Your rate: ", hotel_rate)

print()

val = int(input("Enter positive or negative value: "))

if val < 0:
    val = val

print(-val)

print()

user_age = int(input("Enter your age: "))
if user_age < 25:
    insure_price = 4800
else:
    insure_price = 2200

print(f"Annual price: ${insure_price}")

print()
