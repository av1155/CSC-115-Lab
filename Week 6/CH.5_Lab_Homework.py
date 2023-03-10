# 5.15.1: LAB: Count input length without spaces, periods, exclamation points, or commas
user_text = input("Enter a sentence: ")

special_character_list = [" ", "!", "@", "#", "$", "%", "^", "&", "*",
                          "(", ")", "-", "_", "+", "=", "<", ">", "/", "\\", "|", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "~", "`"]

count = len(user_text)
for char in list(user_text):
    if char in special_character_list:
        count -= 1
print(count, "\n")

##########################################################################
# 5.16 LAB: Password modifier
word = input("Enter a password: ")
password = ""

for character in word:

    if character == "i":
        password += "1"
    elif character == "a":
        password += "@"
    elif character == "m":
        password += "M"
    elif character == "B":
        password += "8"
    elif character == "s":
        password += "$"
    else:
        password += character

password += "!"
print(password, "\n")

##########################################################################
# 5.17 LAB: Output range with increment of 5
first_num = int(input("Please enter your first number: "))
second_num = int(input("Please enter your second number: "))

if (second_num < first_num):
    print("Second integer can't be less than the first.", end="")
else:
    for i in range(first_num, (second_num + 1), 5):
        print(i, end=" ")
print()

##########################################################################
# 5.19 LAB: Countdown until matching digits
number = int(input("\nPlease enter a number: "))
while (number < 11) or (number > 100):
    number = int(input("\nInput must be 11-100: "))

while (number > 11) and (number <= 100):
    print(number)
    number -= 1
    if (number % 11) == 0:
        print(number)
        break

# number = int(input())
# if (number < 11) or (number > 100):
#     print("Input must be 11-100")

# else:
#     while (number >= 11) and (number <= 100):
#         print(number)
#         number -= 1
#         if (number % 11) == 0:
#             print(number)
#             break

##########################################################################
# 5.18 LAB: Print string in reverse
while True:
    text = str(
        input("\nPlease enter text (enter d, or done, or Done to quit): \n"))

    if text == "Done":
        quit()
    elif text == "done":
        quit()
    elif text == "d":
        quit()

    for string in reversed(text):
        print(string, end="")
    print()
