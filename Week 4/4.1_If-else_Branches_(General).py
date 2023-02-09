print("4.1: If-else branches (General)")

# Branch: Sequence of statements only executed under a certain condition.
# If: An if branch is a branch taken only if an expression is true.

hotel_rate = 160
user_age = int(input("Enter your age: "))

if user_age > 65:
    hotel_rate = hotel_rate - 30

print("Your rate: ", hotel_rate)

print()

# If-else Branches
# If-else branch: It has two branches: The first branch is executed if an expression is true, else the other branch is executed.

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

# If-elseif-else Branches
# Commonly a programmer wishes to take one of multiple (three or more) branches. An if-else can be extended to an if-elseif-else structure. Each branch's expression is checked in sequence; as soon as one branch's expression is found to be true, that branch is taken. If no expression is found true, execution will reach the else branch, which then executes.

# Note: The else part is optional. If omitted, then if none of the previous expressions are true, no branch executes.

# If the same branch is repeated later, that branch will never execute because the one that is before will execute first.
