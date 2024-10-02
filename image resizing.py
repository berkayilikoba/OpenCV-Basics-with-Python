
import cv2 as cv

img = cv.imread('bjk.jpg')

width = 1000

height = 1000

dims = (width,height) 

img = cv.resize(img,dims) 

cv.imshow('title', img)

cv.waitKey()

cv.destroyAllWindows() 