import cv2
import numpy as np


font = cv2.FONT_HERSHEY_COMPLEX

# Read the image
img = cv2.imread("D:/Old G drive data/Old G drive data/PatentIdeaPaper/apple1.jpeg")
cv2.imshow("shapes", img)
print(img)

# add color filter
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

# Find the contours in the black and white image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours="+str(len(contours)))

# Selecting maxim contour corresponding to actual surface area
contours = max(contours, key=cv2.contourArea)

# Fitting ellipse to the contour
ellipse = cv2.fitEllipse(contours[1])
(x,y),(ma,MA),angle =ellipse
print("Major Axis:  "+str(MA),"Minor Axis:  "+str(ma))

# Finding the approximate volume of the apple using ellpsoid
Volume = 4*(np.pi)*(MA**2)*(ma)
print("Volume::  "+str(Volume))
img = cv2.ellipse(img, ellipse, (0,255,0),2)

cv2.waitKey(0)
cv2.destroyAllWindows()
