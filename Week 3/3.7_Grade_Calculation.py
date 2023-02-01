exam_1_grade = float(input('Enter your exam 1 grade here (out of 100): '))
exam_2_grade = float(input('Enter your exam 2 grade here (out of 100): '))
exam_3_grade = float(input('Enter your exam 3 grade here (out of 100): '))

exam_grades = [exam_1_grade, exam_2_grade, exam_3_grade]

print(
    f'Your average exam grade is: {(sum(exam_grades) / len(exam_grades)):.2f}')
