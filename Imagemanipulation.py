import cv2
import numpy as np
#read the image
img=cv2.imread("earth.png")
#color conversions
rgb_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#hsv is a very concentrated image
#display the images
cv2.imshow("Original(BGR)",img)
cv2.imshow("RGB Image",rgb_image)
cv2.imshow("Grayscale image",gray)
cv2.imshow("HSV Image",hsv)
#cropping
cropping_section=img[100:300,200:400]
cv2.imshow("Cropped image",cropping_section)
#rotate the image
(h, w) = img.shape[:2]#:2 slices the data
center = (w//2, h//2)#finds the center
M = cv2.getRotationMatrix2D(center, 45, 1.0)#rotate by 45 degrees
rotated = cv2.warpAffine(img, M, (w, h))#warpAffine is used to apply the rotation matix
rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
cv2.imshow("Rotated image",rotated_rgb)
#Add brightness
brightness_matrix = np.ones(img.shape, dtype="uint8") * 50 #dtype="uint8" is used to ensure calues fit in the standard image intensity range(0-255)
brighter = cv2.add(img, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
cv2.imshow("Brighter image",brighter_rgb)
#keep the window open
cv2.waitKey(0)
cv2.destroyAllWindows()
