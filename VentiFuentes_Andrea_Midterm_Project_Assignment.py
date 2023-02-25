print("\nAndrea A. Venti Fuentes")  # Student's Full Name
print("aav66@miami.edu")  # Student's Email
print("CSC 115: Python Programming for Everyone")  # Course
print("B.S. in Computer Science\n")  # Student's Major

# The input below records the starting number of organisms.
starting_num_organisms = int(input("Enter the starting number of organisms: "))
# The while loop below validates the input and requests the user to input a new value if the number is negative or zero.
while starting_num_organisms <= 0:
    starting_num_organisms = int(input(
        "Negative values or zero for the starting number of organisms is not allowed. Please re-enter the starting number of organisms: "))
print()

# The input below records the average daily population increase.
daily_population_increase = float(input(
    "Enter the average daily population increase (number will be translated to percent value, for example, 30 means 30%): "))
# The while loop below validates the input and requests the user to input a new value if the numbers are either negative or larger than 100.
while (daily_population_increase < 0) or (daily_population_increase > 100):
    daily_population_increase = float(input(
        "Negative values or values larger than 100 are not allowed. Please re-enter the average daily population increase: "))

# The equation below converts the value into a decimal and adds 1 to turn it into a positive multiplication value. For example, 30 becomes 1.3, when 1.3 * 2 = 2.6
daily_population_increase = ((daily_population_increase + 100) / 100)

print()

# The input below records the number of days that the organisms will be left to multiply for.
days_to_multiply = int(
    input("Enter the number of days the organism will multiply for: "))
while (days_to_multiply > 30) or (days_to_multiply < 0):
    days_to_multiply = int(input(
        "Negative values or values larger than 30 are not allowed. Please re-enter the number of days the organism will be left to multiply for: "))
print()

print("Day\t Approximate Population")

for days in range(1, (days_to_multiply + 1)):
    print(f"{days} \t {starting_num_organisms:.4f}")
    starting_num_organisms *= daily_population_increase
