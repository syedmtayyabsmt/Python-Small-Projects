def string_and_number_calculator(string):
    checker_dict = {'Lower_case': 0, 'Upper_case': 0, 'Number': 0}

    for letter in string:
        if letter.isupper():
            checker_dict['Upper_case'] = checker_dict['Upper_case'] + 1

        elif letter.islower():
            checker_dict['Lower_case'] = checker_dict['Lower_case'] + 1

        elif letter.isnumeric():
            checker_dict['Number'] = checker_dict['Number'] + 1

        else:
            pass

    print(f"There Are {checker_dict['Upper_case']} Upper Case In Text")
    print(f"There Are {checker_dict['Lower_case']} Lower Case In Text")
    print(f"There Are {checker_dict['Number']} Numbers In Text")


i_string = input('Write Text To Check :: ')

string_and_number_calculator(i_string)
