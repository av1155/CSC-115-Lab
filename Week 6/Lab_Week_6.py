print("Friday 24, 2023")


# Program that makes the second number larger than the first number
first_num = int(input("Enter the first number: "))
while (first_num < 0):
    first_num = int(
        input("The first number must be positive. Please enter another number: "))

second_num = int(input("Enter the second number: "))
while (second_num <= first_num):
    second_num = int(
        input("The second number must larger than the first number. Please enter another number: "))

sum = first_num

while (first_num < second_num):
    first_num += 1
    sum += first_num

print(f"The sum is: {sum}")
