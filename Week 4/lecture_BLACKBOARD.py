# Chapter 4 Lecture: ALL ABOUT DECISION STRUCTURES and BOOLEAN LOGIC

# Here is an example of IF-ELIF-ELSE

averageScore = (float)(input('Enter your grade: '))

if averageScore >= 90:
    print('You got an A.')
elif averageScore >= 80:
    print('You got a B.')
elif averageScore >= 70:
    print('You got a C.')
elif averageScore >= 60:
    print('You got a D.')
else:
    print('You got an F.')

# Here is an example of using NESTED IF-ELSE

if averageScore >= 90:
    print('You earn an A.')
else:
    if averageScore >= 80:
        print('You got a B.')
    else:
        if averageScore >= 70:
            print('You got a C.')
        else:
            if averageScore >= 60:
                print('You got a D.')
            else:
                print('You got an F.')

print('Done.')
