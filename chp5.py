import cv2
import numpy as np

img = cv2.imread("farah\Reading.jpg")

print(img.shape)

#using pithagors 
width, height = 565 ,819 

#get them from windows paint
pts1 = np.float32([[72,272],[621,139],[312,1055],[960,881]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Image" , img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)