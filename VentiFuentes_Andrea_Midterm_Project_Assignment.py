print("Andrea A. Venti Fuentes")  # Full Name
print("aav66@miami.edu")  # Email
print("CSC 115: Python Programming for Everyone")  # Course
print("B.S. in Computer Science")  # Major

# This records the starting number of organisms.
starting_num_organisms = float(
    input("Enter the starting number of organisms: "))

# This records the average daily population increase.
avg_daily_population_increase = float(
    input("Enter the average daily population increase: "))

# This records the number of days that the organisms will be left to multiply for.
num_of_days = float(
    input("Enter the number of days the organism will multiply for: "))

if ((avg_daily_population_increase < 0) or (avg_daily_population_increase > 100)) or (num_of_days > 30):
    print("Error")


# There have to be three inputs.
# Validate program. Number of days has to be between 0 and 100. No negative numbers and no numbers avobe 100. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# No more days than 30 for multiplication.
