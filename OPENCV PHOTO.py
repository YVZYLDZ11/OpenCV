import cv2
import numpy as np

img = cv2.imread("image1.jpg", 0)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.resize(img, (300,300))
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

print(img)
print(img.shape)

img = cv2.imread("Image1.jpg", -1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)
print(img)
print(img.shape)

img = cv2.rectangle(img, (300, 300), (200, 200), (134, 56, 132), 6)