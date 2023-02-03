''' 3.12 LAB: Input and formatted output: Right-facing arrow '''

base_char = input('Input only 1 symbol: ')
head_char = input('Input only 1 symbol: ')

row1 = '      ' + head_char
row2 = base_char * 6 + head_char * 2
row3 = base_char * 6 + head_char * 3

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 3.13 LAB: Phone number breakdown '''

################################################################
print()

numbers = 123456
rightMost2Digits = numbers % 100
print(rightMost2Digits)

div = 123456
leftMost2DigitsDiv = div // 10000
print(leftMost2DigitsDiv)

print()
################################################################

phone_number = int(input("Enter your phone number (unformatted): "))

print(f"({phone_number // 10000000}) {(phone_number % 10000000) // 10000}-{phone_number % 10000}")

'''-----------------------------------------------------------------------------------------------------------------------------------'''
''' 3.15 LAB: Input and formatted output: House real estate summary '''
print()

current_price = int(input("Enter the current price of the property: "))
last_months_price = int(
    input("Enter the last month's price of the property: "))

print(f"This house is ${current_price}. The change is ${current_price + (- last_months_price)} since last month.\nThe estimated monthly mortgage is ${(current_price * 0.051) / 12:.2f}.")
