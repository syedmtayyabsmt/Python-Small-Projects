import cv2 as cv
import webbrowser

camera = cv.VideoCapture(0)

while True:
    success, img = camera.read()
    qrd = cv.QRCodeDetector()
    a, b, c = qrd.detectAndDecode(img)

    if a != '':
        print(a)
        webbrowser.open(a)
        break

    cv.imshow('Preview', img)
    if cv.waitKey(1) == 27:
        break
