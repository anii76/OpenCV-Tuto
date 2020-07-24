import cv2

img = cv2.imread("farah\IMG_20141128_135354.jpg")

print(img.shape)
# it gives height,width, num of channels (bgr)
#(3264, 2448, 3)

#(width,height)
imgResize = cv2.resize(img, (400,600))
print(imgResize.shape)

#select in matrix
#hight, width / begin:end
imgCropped = imgResize[300:550, 30:250]

#cv2.imshow("Output",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)