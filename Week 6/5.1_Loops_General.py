# This prints the MINIMUM value
x = float(input())
y = float(input())
z = float(input())

min = x
if (y < min):
    min = y
if (z < min):
    min = z

print(f"The minimum value is {min}")

# This prints the MAXIMUM value
a = float(input())
b = float(input())
c = float(input())

max = a
if (b > max):
    max = b
if (c > max):
    max = c

print(f"The maximum value is {max}")
