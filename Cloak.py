import cv2
import numpy as np

cap = cv2.VideoCapture(0)

bg = cv2.imread("./bgImage.jpg")

#cv2.imshow("pic",bg)

while(cap.isOpened()):
    ret,frame = cap.read()

    if(ret):
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        yellow = np.uint8([[[10,242,255]]])
        hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
        
        #print(hsv_yellow)  #=> [[[ 28 245 255]]] this printed value is the hsv value of yellow colour   
         
        #threshold the hsv_white value to get only white color
        #standard formula for range of color -
        #lower: hue-10,100,100     ; higher: hue+10,255,255
        #if any color falls out of  this range, we have to remove it        
        lower_yellow = np.array([18,100,100])
        upper_yellow = np.array([38,255,255])
        mask = cv2.inRange(hsv,lower_yellow,upper_yellow)   #it will mask everything(black out) that is out of our range
        #cv2.imshow("mask",mask)     #only yellow objects will be visible

        part1 = cv2.bitwise_and(bg , bg , mask=mask)   #(bg & yellow = True , bg & anyOtherColour = False)
        #cv2.imshow("part1",part1)   #only the background behind cloak is visible rest everything is black

        #now we also want to display our rest of the background
        #so in part2 we will make only the rest of the background visible, for that we have to do just reverse of part1
        #and then we will merge both the parts
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame , frame , mask=mask)
        #cv2.imshow("part2",part2)      #whole  except cloak will be visible

        kernel = np.ones((5,5), np.uint8)
        sharp = cv2.morphologyEx(part1+part2,cv2.MORPH_CLOSE, kernel)
        cv2.imshow("cloak",sharp)    
       
        if(cv2.waitKey(1)==ord("q")):
            break
cv2.destroyAllWindows()
cap.release()
