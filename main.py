from cvzone.HandTrackingModule import HandDetector as Hd
import cv2 as cv
import time
import random as rand
import winsound as win

camera = cv.VideoCapture(0)
detector = Hd(detectionCon=0.8, maxHands=2)

comp_input = ['ROCK', 'PAPER', 'SCISSORS']
comp_choice = rand.choice(comp_input)
user_score, comp_score = 0, 0

while user_score != 5 and comp_score != 5:
    success, img = camera.read()
    hands, img = detector.findHands(img)

    if hands:
        
        time.sleep(1)
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        fingers1 = detector.fingersUp(hand1)

        s1 = str(sum(fingers1))
        sum_of_fingers = sum(fingers1)
        cv.putText(img, s1, (15, 50), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        position = lmList1[8]

        if position[0] >= 550 and position[0] <= 600 and position[1] >= 0 and position[1] <= 40:
            break
    
        user_input = ''

        if sum_of_fingers == 2:
            user_input = 'SCISSORS'
            cv.putText(img, user_input, (300, 100), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            time.sleep(1)
        
        elif sum_of_fingers == 5:
            user_input = 'PAPER'
            cv.putText(img, user_input, (300, 100), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            time.sleep(1)
        
        elif sum_of_fingers == 0:
            user_input = 'ROCK'
            cv.putText(img, user_input, (300, 100), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            time.sleep(1)
        
        elif sum_of_fingers == 4:
            print("Four Fingers Detected (Program Ended)")
            win.Beep(1000, 1500)
            break

        if user_input in comp_input:

            comp_choice = rand.choice(comp_input)

            if user_input == comp_choice:
                print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
                print('DRAW')

            elif (user_input == 'ROCK' and comp_choice == 'PAPER') or (user_input == 'PAPER' and comp_choice == 'SCISSORS') or (user_input == 'SCISSORS' and comp_choice == 'ROCK'):
                comp_score += 1
                print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
                print('Computer Wins')
            
            elif (user_input == 'PAPER' and comp_choice == 'ROCK') or (user_input == 'SCISSORS' and comp_choice == 'PAPER') or (user_input == 'ROCK' and comp_choice == 'SCISSORS'):
                user_score += 1
                print(f'You Choose {user_input} And Computer Choose {comp_choice} | Your Score Is {user_score} And Computer Score Is {comp_score}')
                print('User Wins')
            
            win.Beep(1000, 500)
            time.sleep(1)

    cv.putText(img, 'Exit Game By Showing 4 Fingers ', (55, 40), cv.FONT_ITALIC, 1, (255, 255, 255), 4)

    cv.imshow("Game", img)

    if cv.waitKey(1) == 27:
        break
