employee_data = []

while exit != 'Yes':

    try:   
        id = int(input("Enter Employee's Id No: "))
    except ValueError:
        print('(ERROR) "Enter Number Only"')
        continue

    try:   
        basic_salary = int(input('Input Employee Basic Salary: '))
    except ValueError:
        print('(ERROR) "Enter Number Only"')
        continue

    medical_allowance = (50 * basic_salary) / 100
    convence_allowance = (25 * basic_salary) / 100
    gross_salary = basic_salary + medical_allowance + convence_allowance

    employee_data.append({'Employee Id': id,
                         'Basic Salary': basic_salary,
                         'Medical Allowance': medical_allowance,
                         'Convence Allowance': convence_allowance,
                         'Gross Salary': gross_salary})

    
    exit = input('Do You Want To Exit ? (Enter "Yes" To Exit And "No" To Keep Going): ').capitalize()
    if exit == 'Yes':
        print('Program Ended')
        break
    elif exit == 'No':
        continue
    else:
        while exit != 'Yes' and exit != 'No':
            print('Enter The Right Value')
            exit = input('Do You Want To Exit ? (Enter "Yes" To Exit And "No" To Keep Going): ').capitalize()

print('\n=====================')
print("Data Of All Employees")
print('=====================\n')

for i in employee_data:

    print(f'''
Employee Id Is {i['Employee Id']}
Basic Salary Is {i['Basic Salary']}
Medical Alllowance Is {i['Medical Allowance']}
Convence Allowance Is {i['Convence Allowance']}
Gross Salary Is {i['Gross Salary']}
================================================
================================================''')
