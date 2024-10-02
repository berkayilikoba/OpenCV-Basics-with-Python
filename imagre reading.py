import cv2 as cv

image = cv.imread('bjk.jpg')

cv.imshow('title', image)

cv.waitKey()

cv.destroyAllWindows()