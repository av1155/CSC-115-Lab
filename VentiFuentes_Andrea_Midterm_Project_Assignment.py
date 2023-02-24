print("Andrea A. Venti Fuentes")  # Student's Full Name
print("aav66@miami.edu")  # Student's Email
print("CSC 115: Python Programming for Everyone")  # Course
print("B.S. in Computer Science\n")  # Student's Major

# The input below records the starting number of organisms.
starting_num_organisms = float(
    input("Enter the starting number of organisms: "))
while starting_num_organisms < 0:
    starting_num_organisms = float(input(
        "A negative number for the starting number of organisms is not allowed. Please re-enter your starting number of organisms value: "))

# The input below records the average daily population increase.
avg_daily_population_increase = float(
    input("Enter the average daily population increase: "))
# The while loop below validates the input and requests the user to input a new value if the numbers are either negative or higher than
while (avg_daily_population_increase < 0) or (avg_daily_population_increase > 100):
    avg_daily_population_increase = float(input(
        "Negative values or values higher than 100 are not allowed. Please re-enter your average daily population increase: "))

# The input below records the number of days that the organisms will be left to multiply for.
days_to_multiply = float(
    input("Enter the number of days the organism will multiply for: "))
while (days_to_multiply > 30):
    days_to_multiply = float(input(
        "No more than 30 days is allowed for the number of days to multiply. Please re-enter your days to multiply value: "))

# There have to be three inputs.
# Validate program. Number of days has to be between 0 and 100. No negative numbers and no numbers avobe 100. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# No more days than 30 for multiplication.
