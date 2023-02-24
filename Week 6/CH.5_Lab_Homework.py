# 5.15.1: LAB: Count input length without spaces, periods, exclamation points, or commas
user_text = input("Enter a sentence: ")

special_character_list = [" ", "!", "@", "#", "$", "%", "^", "&", "*",
                          "(", ")", "-", "_", "+", "=", "<", ">", "/", "\\", "|", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "~", "`"]

count = len(user_text)
for char in list(user_text):
    if char in special_character_list:
        count -= 1
print(count)

# # 8 minutes

# # 5.16 LAB: Password modifier
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
print(password)
