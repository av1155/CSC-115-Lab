user_input = input("Enter something: ")

while (user_input != "done") and (user_input != "Done"):
    print(user_input)
    user_input = input("Enter something...")


stop = int(input())
result = 0
for a in range(4):
    for b in range(3):
        result += a + b
    print(result)
    if result > stop:
        break

"""
            RAM
Stop:       
Result:
a:
b:

Output: 
3
9
18

"""
