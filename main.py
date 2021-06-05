import cv2
import time
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputfile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0
for i in range(60):
    ret, bg = cap.read()
bg = np.flip(bg, axis = 1)
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, access = 1)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerred = np.array([0, 120, 50])
    upperred = np.array([10, 255, 255])
    mask1 = cv2.inRange(HSV, lowerred, upperred)
    lowerred = np.array([170, 120, 70])
    upperred = np.array([180, 255, 255])
    mask2 = cv2.inRange(HSV, lowerred, upperred)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEX(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEX(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    mask2 = cv2.bitwisenot(mask1)
    res1 = cv2.bitwiseand(img, img, mask = mask2)
    res2 = cv2.bitwiseand(bg, bg, mask = mask1)
    finaloutput = cv2.addweighted(res1, 1, res2, 0)
    outputfile.write(finaloutput)
    cv2.imshow("Magic", finaloutput)
    cv2.waitKey(1)
cap.release()
out.release()
cv2.destroyAllWindows()
