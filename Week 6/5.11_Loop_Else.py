# 5.11 Loop else

total = 0
for i in range(1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        total += 1
        print(f"{i} is divisile by 3 and 5.")
    else:
        print(f"{i} is not divisile by 3 and 5.")
print(f"The amount of numbers that are divisible by 3 and 5 is: {total}\n")

# Loop else branch taken if loop completes normally
names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end=' ')
else:
    print('All names printed.\n')

# Loop else: Executes if the loop completes normally. In the example above, "all names printed" will show if all of the names are printed.

x = 0
y = 5
z = 10
while x < y:
    if x == z:
        print('x == z')
        break
    x += 1
else:
    print('x == y')


result = 1
n = 2
while n > -1:
    print(n, end=' ')
    result *= 4
    n -= 1
else:
    print(f'| {result}')
print('done')

# 2 1 0 | 64
# done
