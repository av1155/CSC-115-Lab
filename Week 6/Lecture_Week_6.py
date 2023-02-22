counter = 1

while (counter <= 5):
    print(counter, "Chapter 5 Lecture: Repetition Structures")
    counter = counter + 1

print("Program Complete")

########################################################################

counter = 1
sum = 0

while (counter <= 10):
    sum = sum + counter
    # if the sum is printed at the end of the loop, it will print indefinitely until program crashes. In this case, if it is printed before the counter = counter + 1, it will just print the sum until it gets to the final result.
    print(sum)
    counter = counter + 1
    # if print is placed indented in the loop, it will print after every iteration of the program. If not, it will just print once with the final result.
print("The sum from 1 to 10 is: ", sum)

print("Program Complete")

########################################################################

# while (condition):        # if conidition is true, then loop body will be executed
#     -> loop body          # an iteration is the number of times the loop is executed. For example, the code above has 100 interations, because when the _______                       counter is equal to 101 the loop stops.

########################################################################

number_exams = 4
counter = 1  # Counter is a variable to keep track of the number of times the loop is executed
sum = 0.0

while (counter <= number_exams):

    exam_score = float(input("Enter your exam score: "))
    # input validation (no negative numbers or greater than 100 allowed)
    while (exam_score < 0 or exam_score > 100):
        exam_score = float(
            input("Invalid input. Please enter a valid exam score: "))

        # The difference between if else and while loop in this scenario is that if the if else is true, it goes ahead with the rest of the program. In a while loop, it will keep sending you back if a wrong exam score is entered.

    sum = sum + exam_score
    counter = counter + 1

average_score = sum / number_exams
print(average_score)

print("Program Complete")
