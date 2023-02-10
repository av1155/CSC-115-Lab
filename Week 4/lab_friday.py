'''
print("Week 4 Lab")

name = input("What is your name? ")

year_born = int(input("What year were you born? "))

age = 2023 - year_born

print("Hello " + str(name) + "! You are " + str(age) + " years old.")

if (age >= 18):  # After If condition has to follow
    print("You can vote now.")
else:  # After else colon has to follow
    print("You cannot vote. Just wait.")

print("Program complete")
'''

'''
FirstStudentName = input("Enter a name: ")
SecondStudentName = input("Enter a name: ")

if (FirstStudentName < SecondStudentName):
    print(FirstStudentName)
    print(SecondStudentName)

else:
    print(SecondStudentName)
    print(FirstStudentName)

print("Program complete")
'''

'''
testScore = float(input("Enter your average test score: "))

if (testScore >= 90):
    print("Yout got an A")
elif (testScore >= 80):
    print("You got a B")
elif (testScore >= 70):
    print("You got a C")
elif (testScore >= 60):
    print("You got a D")
else:
    print("You got an F")

if (testScore == 100):
    print("Congratulations! You earned a perfect test score")
'''

# Given 3 numbers: X, Y, and Z. Find minimum.
x = int(input())
y = int(input())
z = int(input())

if (y < x):
    min = y
if (z < min):
    print(min)
if (x < y) and (x < z):
    min = x
    print(min)
elif (y < x) and (y < z):
    min = y
    print(min)
else:
    min = z
    print(min)
