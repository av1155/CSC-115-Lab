# CORRECT SYNTAX

name = "Andrea Venti Fuentes"

gpa = 4.0

major = "Computer Science"

age = 22

print(name + ", " + str(gpa) + ", " + major + ", " + str(age))

print(f"{name}, {str(gpa)}, {major}, {str(age)}")

print()

# CORRECT SYNTAX

# Arithmetic
# +
# -
# *
# /
# %

# Relational Operators
# < >
# <= >=
# ==
# != <>

age = int(input("How old are you? "))

if (age >= 21):
    print("You can drink.")
else:  # Else is not followed by a conditon, it uses the if coniditon.
    print("You cannot drink.")

print("Program Complete.")

print()

your_score = float(input("What is your score? "))

if (your_score >= 90):
    print("You got an A")

elif (your_score >= 80):
    print("You got a B")

elif (your_score >= 70):
    print("You got a C")

elif (your_score >= 60):
    print("You got a D")

else:
    print("You got an F")
