import cv2 as cv

img = cv.imread('bjk.jpg')

#method 1
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('method 1', gray_image)

#method 2
img = cv.imread('bjk.jpg', 2)

cv.imshow('method2', img)
cv.waitKey()
cv.destroyAllWindows()
