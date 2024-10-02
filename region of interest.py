import cv2 as cv

img = cv.imread("bjk.jpg")


x,y,w,h = cv.selectROI(img)


selected = img[(y):(y+h),(x):(x+w)]

cv.imshow('region of interes', selected)

cv.waitKey()

cv.destroyAllWindows()