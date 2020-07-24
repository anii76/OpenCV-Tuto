import cv2

cap = cv2.VideoCapture(0)

#width/height/brightness
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

myColors = []

def findColor(img):
  imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  lower = np.array([h_min, s_min, v_min])
  upper = np.array([h_max, s_max, v_max])
  mask = cv2.inRange(imgHSV, lower, upper)
  cv2.imshow("img", mask)

#exit when 'q' typed
while True:
  success, img = cap.read()
  cv2.imshow("type q to exit",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break

