from cvzone.HandTrackingModule import HandDetector as Hd
import cv2 as cv

camera = cv.VideoCapture(0)
detector = Hd(detectionCon=0.8, maxHands=2)

while True:

    success, img = camera.read()
    hands, img = detector.findHands(img)

    if hands:

        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        fingers1 = detector.fingersUp(hand1)

        s1 = str (sum(fingers1))
        cv.putText(img,s1,(25,50),cv.FONT_HERSHEY_PLAIN,3,(0,0,255),3 )

        pos = lmList1[8]
        print(pos)

        if pos[0] >= 550 and pos[0] <= 600 and pos[1] >= 0 and pos[1] <= 40:
            break

    cv.putText(img, 'Exit Here --> ', (320, 50), cv.FONT_ITALIC, 1, (255, 255, 255), 4)
    cv.circle(img, (600, 40), 40, (255, 255, 255), 2)

    cv.imshow("Preview", img)

    if cv.waitKey(1) == 27:
        break
