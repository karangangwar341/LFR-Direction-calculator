import math
import cv2 as cv
import numpy as np
img = cv.imread("05.png")
Blank = np.zeros((img.shape))
cv.imshow("given",img)
img = cv.resize(img, (400,400))
edge = cv.Canny(img, 500, 1000, apertureSize=5, L2gradient=True )
#cv.imshow("image", edge)

#Finding contours in the image
contours, hierarchy = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#Printing out the number of contours
print("Number of Contours found = " + str(len(contours)))

#Drawing out the contours on a blank image
cv.drawContours(Blank, contours, -1, (0,255,0), 0)

#Checking if the image is of an intersection or not
if (len(contours)>2):
    print("The image is of an intersection")
else:
    c = contours[0]
    c2 = contours[1]
    extr = tuple(c[c[:, :, 0].argmin()][0])
    extl = tuple(c[c[:, :, 0].argmax()][0])
    extr1 = tuple(c2[c2[:, :, 0].argmin()][0])
    resr=""
    resl=""
    resr1=""
    for i in extr:
        resr+=str(i)
        break
    resr= int(resr)
    for i in extl:
        resl+=str(i)
        break
    resl= int(resl)
    for i in extr1:
        resr1+=str(i)
        break
    resr1= int(resr1)
    offset = (resr1 - resr)/2
   # print(resr1,resr)
    if offset < 0:
        offset= offset*(-1)
    angle = (resr - resl)/400
    if angle < 0:
        angle= angle*(-1)
    offangle = math.atan(angle)
    offangle = math.degrees(offangle)
  #  print(resr,"  ",resl,"  ",resr1)
    print("offset distnace     =", offset)
    print("offset angle        =", offangle)

cv.imshow("Contours", Blank)

cv.waitKey(0)