import cv2
import numpy as np

#AND: A bitwise AND is true if and only if both pixels are greater than zero.
#OR: A bitwise OR is true if either of the two pixels is greater than zero.
#XOR: A bitwise XOR is true if and only if one of the two pixels is greater than zero, but not both.
#NOT: A bitwise NOT inverts the “on” and “off” pixels in an image.


image1 = np.zeros((300, 300), dtype="uint8")

cv2.circle(image1, (150, 150), 100, 255, -1)

image2 = np.zeros((300, 300), dtype="uint8")

cv2.rectangle(image2, (50, 50), (250, 250), 255, -1)

# 5. Bitwise AND işlemi
bitwise_and = cv2.bitwise_and(image1, image2)

# 6. Bitwise OR işlemi
bitwise_or = cv2.bitwise_or(image1, image2)

# 7. Bitwise XOR işlemi
bitwise_xor = cv2.bitwise_xor(image1, image2)

# 8. Bitwise NOT işlemi (image1'in tersi)
bitwise_not = cv2.bitwise_not(image1)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)

cv2.waitKey()