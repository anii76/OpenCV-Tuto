import cv2

#0 is camera id (device himself)
cap = cv2.VideoCapture(0)

#capture details
#width/height/brightness
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

#exit when 'q' typed
while True:
  success, img = cap.read()
  cv2.imshow("type q to exit",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

