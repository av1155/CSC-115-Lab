population = int(input("Enter the starting number of organisms: "))
DailyIncrease = float(input(
    "Enter the average daily population increase (number will be translated to percent value, for example, 30 means 30%): "))
DailyIncrease = ((DailyIncrease + 100) / 100)
Days = int(input("Enter the number of days the organism will multiply for: "))
print("Day Approximate\t Population")
for i in range(1, Days + 1):
    print(i, "\t\t", population)
    population = population * DailyIncrease
