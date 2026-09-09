import cv2
import numpy as np
#read the image
image=cv2.imread('earth.png')
if image is None:
    print("Image not found")
    exit()
#convert image to gray scale
gray=cv2.cvt.Color(image,cv2.COLOR_BGR2GRAY)
#Menu-pick options from
print("Choose and option")
print("1. Apply Gaussian Blur")
print("2. Apply median Blur")
print("3. Canny Edge Detection")
print("4. Sobel Edge Detection")
print("5. Laplacian Edge Detection")
print("6. Exit")
while True:
    choice=int(input("Enter a choice:"))
    #gausian blur
    if choice==1:
        blur=cv2.GaussianBlur(gray,(5,5),0)#(5,5) is the strength of the blur
        cv2.imshow("Gaussian Blur",blur)
    #median filter
    elif choice==2:
            median=cv2.medianBlur(gray,5)#(5,5) is the strength of the blur
            cv2.imshow("Median Blur",median)
    #canny edge detection
    elif choice==3:
         edges=cv2.Canny(gray,100,200)#outline the edges of the image
         cv2.imshow("Canny Edge Detection",edges)
    #sobel edge detection
    elif choice==4:
         #starting point
         sobelx=cv2.Sobel(gray,cv2.CV_16F,1,0,ksize=5)
         sobely=cv2.Sobel(gray,cv2.CV_16F,0,1,ksize=5)
         #apply the flter
         sobel=cv2.magnitude(sobelx,sobely)
         cv2.imshow("Sobel Edge Detection",sobel)
    #Laplacian edge detection
    elif choice==5:
         laplacian=cv2.Laplacian(gray,cv2.CV_16F)
         cv2.imashow("Laplacian Edge Detection",laplacian)
    #close program
    elif choice==6:
        break
    else:
         print("Invalid choice. Please try again.")
    