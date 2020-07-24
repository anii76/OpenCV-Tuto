import cv2

cap = cv2.VideoCapture("D:\My Files\Phone\VID_20200428_105649.mp4")

#exit when 'q' typed
while True:
  success, img = cap.read()
  cv2.imshow("type q to exit",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

