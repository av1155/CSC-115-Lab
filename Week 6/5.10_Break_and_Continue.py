# 5.10 Break and continue

# Break: A break statement in a loop causes the loop to exit immediately.

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print(f'${meal_cost} buys {num_empanadas} empanadas and {num_tacos} tacos without change.')
else:
    print('You cannot buy a meal without having change left over.')

print("Program Complete!\n")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

mult = 0
while a < 10:
    mult = b * a
    if mult > c:
        break
    a = a + 1
z = a
print(z)

print("Program Complete!\n")

# Continue Statements
# Continue: A continue statement in a loop causes an immediate jump to the while or for loop header statement.

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print(
                f'${meal_cost} buys {num_empanadas} empanadas and {num_tacos} tacos without change.')
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')

print("\n")

stop = 7
result = 0
for n in range(10):
    result += n * 4
    if result > stop:
        break
    print(n)
print(result)

print("\n")

result = 0
for n in range(5):
    result = n - 2
    if (result % 2) != 0:
        print('-', end=' ')
        continue
    print(result, end=' ')
print('done')

print("\n")

a = 2
b = 22
c = 30
result = 0
while a < b:
    result = a * 2
    print(result)
    if result > c:
        break
    a += 3

print("\n")

stop = 14
result = 0
for a in range(3):
    for b in range(4):
        result += a * b
    print(result)
    if result > stop:
        break

print("\n")

stop = 5
result = 0
for a in range(2):
    print(a, end=': ')
    for b in range(3):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()

print()
# 5.10.2: Simon says.
'''
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. Create a for loop that compares each character of the two strings. For each matching character, add one point to user_score. Upon a mismatch, end the loop.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
User score: 4
'''
user_score = 0
simon_pattern = input("Enter text or numbers: ")
user_pattern = input("Enter similar text or numbers: ")

for i in simon_pattern:
    if user_pattern[user_score] == simon_pattern[user_score]:
        user_score += 1
    else:
        break

print(f'User score: {user_score}')

'''
Using index to iterate through each loop you need some number that increases as you go through each iteration. you can just use user_score since it is already assigned to 0, and going to increase after each iteration by 1. You will probably say "but it is going to be increased only if there is a match!" (this is right)! but if there is mismatch you are going to break out of the loop anyways, and end the game so this it's a perfect.
'''
