#filter colouring on photo

import cv2 as cv
import numpy as np

img = cv.imread('bjk.jpg')

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# Threshold of red in HSV space
lower_red = np.array([60, 35, 140])

upper_red = np.array([180, 255, 255])

mask = cv.inRange(hsv, lower_red, upper_red)

result = cv.bitwise_and(img, img, mask=mask)

cv.imshow('frame', img)

cv.imshow('mask', mask)

cv.imshow('result', result)

cv.waitKey()