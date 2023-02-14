# 4.9 Membership and identity operators

# Membership operators: in/not in
prices = ["$20", 15, 5]
print("$20" in prices)
print(2 in prices)
print(13 not in prices)

print()

# Look for a specific word in the list.
real_madrid_roster = ["Rodrygo", "Casemiro", "Courtois", "Casemiro", "Alaba",
                      "Mendy", "Vinicius", "Valverde", "Kroos", "Modric", "Benzema", "Asensio", "Hazard"]

name = input("Enter a name of a player: ")

if name in real_madrid_roster:
    print(f"We found {name} in the roster.")
else:
    print(f"We did not find {name} in the roster.")

# Look for a specific word in the entire string.
request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')

# Identity operators: is/is not
# The programmer can use the identity operator "is" to check whether two operands are bound to a single object. The inverse identity operator "is not" gives the negated value of "is". Thus, if x is y is True, then x is not y is False.

x = 1
y = 1

if x is y:
    print("Yay")
if x is not y:
    print("Nay")

# A good practice is to avoid using the identity operators "is" and "is not", unless explicitly testing whether two objects are identical.

# The id() function can be used to retrieve the identifier of any object. If x is y is True, then id(x) == id(y) is also True.

x = 1
y = 1

if x is y:  # If this is true
    id(x) == id(y)  # Then this is true too

print()

w = 500
x = 500 + 500  # Create a new object with value 1000
y = w + w      # Create a second object with value 1000
z = x          # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('z and y are NOT bound to the same object')


# NOTE: "IS IN" DOES NOT EXIST. THE OPERATOR USED WOULD BE "IS".
