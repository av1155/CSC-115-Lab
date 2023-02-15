# Lecture Notes

'''
# Variables to represent the base hours and the overtime multiplier
base_hours = 40 # Base hours per week
ot_multiplier = 1.5 # Overtime multiplier

# Get the hours worked and the hourly pay rate
hours = float(input("hours worked"))
pay_rate = float(input("hourly"))
'''

hourly_rate = 10.0  # Hourly rate: 10.0
overtime_multiplier = 2.0  # Overtime multiplier: 2.0

weekly_work_hours = float(input("Enter your weekly work hours: "))

if (weekly_work_hours > 40):
    total_gross_salary = (
        40 * hourly_rate) + ((weekly_work_hours - 40) * overtime_multiplier * hourly_rate)
else:
    total_gross_salary = (weekly_work_hours * hourly_rate)

print(f"You worked {weekly_work_hours} hours. Your hourly rate is ${hourly_rate:.2f}. Your weekly gross salary is ${total_gross_salary:.2f}.")
