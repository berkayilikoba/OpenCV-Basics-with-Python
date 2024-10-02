#erosion (aşındırma)

import cv2 as cv #cv2 cv olarak import edildi

import numpy as np #numpy np olarak import edildi

img = cv.imread('bjk.jpg',2) #resmi import ettik ve griye çevirdik

kernel = np.ones((3,3),dtype=np.uint8) #3x3 boyutunda bir matris oluşturuldu ve türüne resim denildi

result = cv.erode(img,kernel,iterations=1) #resim erode edildi
                                           # buradaki iterations resme kaç kere erode uygulanacağıdır
                                           #iterations büyürse resim daha çok aşınır
cv.imshow("Erosion",result)

#dilation (genişleme)

result1 = cv.dilate(img,kernel,iterations=1)

cv.imshow('Dilation', result1)

cv.waitKey(0)