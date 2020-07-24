import cv2
import numpy as np

print("package imported")

img = cv2.imread("farah\April.jpg")
#matrix 5 by 5
kernel = np.ones((5,5), np.uint8)

#grey img
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur img               kernel(same num) sigma = 0  ascendant value 
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#edges (only edges in image (lines)) numbers define sharpness ++
imgCanny = cv2.Canny(img, 150, 200)

#thickness of edges
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)

#thiness
imgErroded = cv2.erode(imgDialation, kernel, iterations = 1)

#cv2.imshow("Blur",imgBlur)
#cv2.imshow("Gray" , imgGray)
cv2.imshow("Img", img)
cv2.imshow("Canny" , imgCanny)
cv2.imshow("Dialation" , imgDialation)
cv2.imshow("Eroded" , imgErroded)

cv2.waitKey(0)
