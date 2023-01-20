print('To reverse a number')

number = int(input("Please enter a number: "))

reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number = number // 10

print("The reversed number is: {}".format(reversed_number))

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

print('price after tax')

price = float(input("Enter the price: "))
tax = float(input("Enter the tax: "))
total_price = price + (price * tax)
print("Total price: ", total_price)
