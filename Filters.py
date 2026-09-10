import cv2
import numpy as np
#function-to apply the filter
def apply_filter(image,filter_type):
    #copy the image
    filtered_image=image.copy()
    #red tint-remove blue and green
    if filter_type=="red":
        filtered_image[:,:,1]=0 #remove green
        filtered_image[:,:,0]=0 #remove red
    #green tint-removed red and blue
    if filter_type=="green":
        filtered_image[:,:,2]=0 #remove red
        filtered_image[:,:,0]=0 #remove blue
    #blue tint
    if filter_type=="blue":
        filtered_image[:,:,1]=0 #removes green
        filtered_image[:,:,2]=0 #removes red
    if filter_type=="increase": #increase blue
        filtered_image[:,:,0]=cv2.add(filtered_image[:,:,0],50)
    if filter_type=="decrease": #decrease green
        filtered_image[:,:,1]=cv2.subtract(filtered_image[:,:,1],50)
    return filtered_image
#Load the image
img=cv2.imread('earth.png')
filter_type="original"
#menu
print("Press the following keys to apply the filter")
print("r-red")
print("g-green")
print("b-blue")
print("i-increase blue")
print("d-decrease green")
print("q-quit")
while True:
    #apply the filter on the image
    filtered_image=apply_filter(img,filter_type)
    #display the filtered image
    cv2.imshow("Filtered Image",filtered_image)
    key=cv2.waitKey(0) & 0XFF
    if key==ord('r'):
        filtered_image="red"
    if key==ord('g'):
        filtered_image="green"
    if key==ord('b'):
        filtered_image="blue"
    if key==ord('i'):
        filtered_image="increase"
    if key==ord('d'):
        filtered_image="decrease"
    if key==ord("q"):
        break
cv2.destroyAllWindows()