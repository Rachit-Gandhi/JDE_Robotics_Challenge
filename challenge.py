from GUI import GUI
from HAL import HAL
import cv2
import numpy as np
import math
import time
# Enter sequential code!

while True:
    errot=0
    prev_errror=0
    prev_time=0
    sum_error=0
    img = HAL.getImage()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    M = cv2.moments(mask)
    center_x = mask.shape[1]/2
    try:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    except:
        cx = center_x
        cy = 0
    cv2.circle(img, (cx, cy), 10, (0,255,255), -1)
    GUI.showImage(img)
    error = center_x - cx
    if(error < -1):
        HAL.setW(-1)
    elif(error > 1):
        HAL.setW(1)
    if(abs(error) > 1):
        HAL.setV(1)
    # Enter iterative code!                 