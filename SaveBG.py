#To save the background image

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,bg = cap.read()

    cv2.imshow("bgImage",bg)

    if(cv2.waitKey(5) == ord("q")):
        cv2.imwrite("bgImage.jpg",bg)
        break
cv2.destroyAllWindows()
cap.release()

