import winsound as win

employee_data = []

while exit != 'Y':

    name = input("Enter Employee's Name: ")

    try:   
        basic_salary = int(input('Input Employee Basic Salary: '))
    except ValueError:
        print('(ERROR) "Enter Number Only"')
        continue

    medical_allowance = (50 * basic_salary) / 100
    convence_allowance = (25 * basic_salary) / 100
    gross_salary = basic_salary + medical_allowance + convence_allowance

    if gross_salary > 50000:
        tax_value = 4
        income_tax = (tax_value*gross_salary)/100
        net_salary = gross_salary - income_tax

    elif gross_salary <= 50000:
        tax_value = 2
        income_tax = (tax_value*gross_salary)/100
        net_salary = gross_salary - income_tax


    employee_data.append({'Employee Name': name,
                         'Basic Salary': basic_salary,
                         'Medical Allowance': medical_allowance,
                         'Convence Allowance': convence_allowance,
                         'Gross Salary': gross_salary,
                         'Income Tax': income_tax,
                         'Tax Value': tax_value,
                         'Net Salary': net_salary})

    
    exit = input('Do You Want To Exit ? (Enter "Y" To Exit And "N" To Keep Going): ').capitalize()

    if exit == 'Y':
        print('Program Ended')
        win.Beep(1000,1000)
        break
    
    elif exit == 'N':
        win.Beep(1000,500)
        continue
    
    else:
        while exit != 'Y' and exit != 'N':

            print('Enter The Right Value')
            exit = input('Do You Want To Exit ? (Enter "Yes" To Exit And "No" To Keep Going): ').capitalize()
            
            if exit == 'Y':
                win.Beep(1000,1000)
                print('Program Ended')

            elif exit == 'N':
                win.Beep(1000,500)
                continue

            else:
                win.Beep(1000,100)


print('\n=====================')
print("Data Of All Employees")
print('=====================\n')

for i in employee_data:

    print(f'''
Employee Name Is {i['Employee Name']}
Basic Salary Is {i['Basic Salary']}
Medical Alllowance Is {i['Medical Allowance']}
Convence Allowance Is {i['Convence Allowance']}
Gross Salary Is {i['Gross Salary']}
Income Tax On Salary Is {i['Income Tax']} Which Is {i['Tax Value']}%
Your Net Salary Is {i['Net Salary']}
================================================
================================================''')
