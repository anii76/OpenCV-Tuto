import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

paths = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg"]
for path in paths :
 img = cv2.imread(path)
 imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 faces = faceCascade.detectMultiScale(imgGray,1.1,4)

 for (x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255), 2)

 cv2.imshow("Result", img)
 cv2.waitKey(0)