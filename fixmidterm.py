population = int(input("Enter the starting number of organisms: "))
DailyIncrease = float(input("Enter the average daily increase: "))
MultiplyingDays = int(input("Enter the number of days they will multiply: "))
DailyIncrease /= 100  # Convert to decimal

print("Day Approximate\tPopulation")

for CurrentDay in range(1, MultiplyingDays + 1):
    print(CurrentDay, "\t\t", round(population, 5))
    population += population * DailyIncrease
