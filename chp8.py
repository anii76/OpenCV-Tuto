import cv2
import numpy as np

def getContours(img):
  contours, heierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area)
#img src, cntours counter, number (-1 = all) , color, thickness
    if area < 9000:
      cv2.drawContours(imi, cnt, -1, (0,255,0),3)
      par = cv2.arcLength(cnt, True)
      print(par)
      approx = cv2.approxPolyDP(cnt, 0.02*par, True)
      #gives shape according to the numof edges
      print(len(approx))
      objCor = len(approx)
      x, y, w ,h = cv2.boundingRect(approx)

      if objCor == 3: objectType = "Tri"
      elif objCor == 4 : 
         aspRaito = w/float(h)
         if aspRaito > 0.95 and aspRaito < 1.05:
            objectType = "Seq"
         else : objectType = "Rec"
      elif objCor >4 : objectType = "Cir" 
      else : objectType = "None"
      
      cv2.rectangle(imi, (x,y), (x+w , y+h), (0,0,255),2)
      cv2.putText(imi, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,0), 1)
      

path = "farah\paint.png"
img = cv2.imread(path)
#img = cv2.resize(imgi, (250,250))
imi = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = cv2.cvtColor(np.zeros_like(img),cv2.COLOR_BGR2GRAY)
getContours(imgCanny)

'''
#non resized img 
imgiGray = cv2.cvtColor(imgi, cv2.COLOR_BGR2GRAY)
imgiBlur = cv2.GaussianBlur(imgiGray,(7,7),1)
imgiCanny = cv2.Canny(imgiBlur,50,50)
print('not resized')
getContours(imgiCanny)
'''

hor1 = np.hstack((img,cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR), imi ))
hor2 = np.hstack((imgGray,imgBlur, imgBlank))

hor = np.vstack((hor1, cv2.cvtColor(hor2, cv2.COLOR_GRAY2BGR) ))


#cv2.imshow("Original", img)
#cv2.imshow("Blur",imgBlur)
#cv2.imshow("Gray" , imgGray)
cv2.imshow("stacked", hor)
cv2.waitKey(0)