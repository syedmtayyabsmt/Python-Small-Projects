import random as rand

comp_input = ['R','P','S']
comp_choice = rand.choice(comp_input)
user_score,  comp_score = 0, 0

while (user_score != 5 and comp_score != 5):

    print('===================================================================================================================')
    user_input = input('Enter || "R" For ROCK || "P" For PAPER || "S" For SCISSORS: || "EXIT" To End The Game: ').upper()
    comp_choice = rand.choice(comp_input)
#------------------------------------------------------------------------------------------------------------------------------------------
    if (user_input == comp_choice):
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('DRAW')
#------------------------------------------------------------------------------------------------------------------------------------------
    elif (user_input == 'R' and comp_choice == 'P'):
        comp_score += 1
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('Computer Win')
    elif (user_input == 'R' and comp_choice == 'S'):
        user_score += 1
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('User Win')
#------------------------------------------------------------------------------------------------------------------------------------------
    elif (user_input == 'P' and comp_choice == 'S'):
        comp_score += 1
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('Computer Win')
    elif (user_input == 'P' and comp_choice == 'R'):
        user_score += 1
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('User Win')
#------------------------------------------------------------------------------------------------------------------------------------------
    elif (user_input == 'S' and comp_choice == 'R'):
        comp_score += 1
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('Computer Win')
    elif (user_input == 'S' and comp_choice == 'P'):
        user_score += 1
        print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
        print('User Win')
#------------------------------------------------------------------------------------------------------------------------------------------
    elif (user_input == 'EXIT'):
        print('''=========
Game Over
=========''')
        break
#------------------------------------------------------------------------------------------------------------------------------------------
    else:
        print('Enter The Right Value')
