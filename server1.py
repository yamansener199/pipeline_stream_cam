import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

while(cap.isOpened()):

    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    if ret == True: 

        both = np.concatenate((frame, frame1), axis=1)
    else: 
        break

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()