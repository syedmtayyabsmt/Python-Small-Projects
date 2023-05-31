import cv2 as cv

camera = cv.VideoCapture(0)

while True:
    success, img = camera.read()
    cv.putText(img, 'Syed M Tayyab', (100, 50), cv.FONT_ITALIC, 2, (150, 100, 50), 5)

    for i in range(230, 390, 40):
        cv.circle(img, (i, 100), 30, (100, 100, 100), 5)

    cv.imshow('Preview', img)
    if cv.waitKey(1) == 27:
        break
