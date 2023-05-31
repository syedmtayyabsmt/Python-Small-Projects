print('Grade Calculation System')
print('''---------------------------
---------------------------''')

# Input
maths = int(input('Enter Marks For Maths: '))
chemistry = int(input('Enter Marks For Chemistry: '))
physics = int(input('Enter Marks For Physics: '))

# Overall Grade
overall_grade = ((maths + physics + chemistry) * 100) / 300

if(overall_grade >= 80):
    print(f'You Got A+ Grade And Your % Is {overall_grade}')
elif(overall_grade >= 70):
    print(f'You Got A Grade And Your % Is {overall_grade}')
elif(overall_grade >= 60):
    print(f'You Got B Grade And Your % Is {overall_grade}')
elif(overall_grade >= 50):
    print(f'You Got C Grade And Your % Is {overall_grade}')
elif(overall_grade < 50):
    print(f'You Got F Grade And Your % Is {overall_grade}')
print('---------------------------')
