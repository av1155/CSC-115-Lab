# Loop: program construct that repeatedly executes the loop's statements (known as the loop body) while the loop's expression is true; when the expression is false, execution proceeds past the loop. Each time through a loop's statements is called an iteration.

num_list = [2, 4, 9, -1]

sum1 = 0
number = 0

i = 0
while (i < len(num_list)):
    sum1 = sum1 + num_list[i]
    i = i+1

avg = sum1 / len(num_list)
print("The sum is ", sum1)
print(f"The average is {avg}")

print()
