import cv2 as cv
import time
import winsound as win

total = 0
camera = cv.VideoCapture(0)

while True:
    success, img = camera.read()
    qrd = cv.QRCodeDetector()
    a, b, c = qrd.detectAndDecode(img)

    if a != '':
        if a == 'Vegetables':
            time.sleep(1)
            win.Beep(1000, 500)
            total += 800
            print('800 For Vegetables')
            print(f'Your Total Bill Is {total}')

        elif a == 'Laptop':
            time.sleep(1)
            win.Beep(1000, 500)
            total += 50000
            print('50000 For Laptop')
            print(f'Your Total Bill Is {total}')

        elif a == 'Dry Fruits':
            time.sleep(1)
            win.Beep(1000, 500)
            total += 4000
            print(f'4000 For Fruits')
            print(f'Your Total Bill Is {total}')

        elif a == 'Cooking Oil':
            time.sleep(1)
            win.Beep(1000, 500)
            total += 500
            print(f'500 For Cooking Oil')
            print(f'Your Total Bill Is {total}')

        continue

    cv.imshow('Preview', img)
    if cv.waitKey(1) == 27:
        break
