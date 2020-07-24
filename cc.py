import cv2
import numpy as np

width, height = 226, 359 
img = cv2.imread("mytof.jpg")

pts1 = np.float32([[107,610], [464,644], [410,865], [14,816]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image" , img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)