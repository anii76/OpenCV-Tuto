import cv2
import numpy as np

def empty(a) :
   pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
# , window , min value , max value (hue value 360 but we dnt have it in cv2) , call a func everytime if smth changes in trackbar
cv2.createTrackbar("Hue Min","TrackBars",0,179, empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179, empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255, empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255, empty)
cv2.createTrackbar("Val Min","TrackBars",25,255, empty)
cv2.createTrackbar("Val Max","TrackBars",117,255, empty)

while True:
 imgi = cv2.imread("farah\img.jpg")
 
 img = cv2.resize(imgi, (282,282))

 imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
 hor1 = np.hstack((img, imgHSV))

 h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
 h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
 s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
 s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
 v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
 v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
 print(h_min,h_max,s_min,s_max,v_min,v_max)
 
 lower = np.array([h_min, s_min, v_min])
 upper = np.array([h_max, s_max, v_max])
 mask = cv2.inRange(imgHSV, lower, upper)

 imgResult = cv2.bitwise_and(img, img, mask= mask)
 
 hor2 = np.hstack((imgResult, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) ))
 
 ver = np.vstack((hor1, hor2))

 #cv2.imshow("Image", img)
 #cv2.imshow("ImageHSV", imgHSV)
 #cv2.imshow("Mask", mask)
 #cv2.imshow("ImageResult", imgResult)
 cv2.imshow("Collage", ver)
 if cv2.waitKey(1) & 0xFF == ord('q'):
   break