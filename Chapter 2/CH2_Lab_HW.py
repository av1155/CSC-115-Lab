''' 2.13 Lab: Divide input integers '''

user_num = int(input())
div_num = int(input())

result = user_num // div_num

result_2 = result // div_num

result_3 = result_2 // div_num

print(result, result_2, result_3)

''' 2.13 Lab: Driving costs '''

print()


''' OUTPUT the gas cost for 25, 75, and 500 miles.
    INPUT gas_mileage, and gas_cost '''

distance = 20
distance_2 = 75
distance_3 = 500
gas_mileage = float(input())
gas_cost = float(input())

result1 = (distance / gas_mileage) * gas_cost
result2 = (distance_2 / gas_mileage) * gas_cost
result3 = (distance_3 / gas_mileage) * gas_cost

print(f'{result1:.2f} {result2:.2f} {result3:.2f}')