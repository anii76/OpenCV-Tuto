import cv2
import numpy as np

img = cv2.imread("farah\img.jpg")
print(img.shape)

#they have to have same kernal/channel idk lol 
hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv2.imshow("Image0" , hor)
cv2.imshow("Image1" , ver)
cv2.waitKey(0)