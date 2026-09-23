import cv2
import numpy as np
cam=cv2.VideoCapture(0)
#menu
print("""Keyboard Controls:
b-Blue tint
r-red tint
g-green tint
x-Gausian blur
c-canny edge detection
m-median filter
l-laplacian edge detection
s-sobel edge detection
q-quit"""
)
mode="n"
while True:
    success,frame=cam.read()
    if not success:
        print("Error: could not read frames")
        break
    output=frame.copy()
    if mode=="b": #blue is 0
        #blue tint
        output[:,:,1]=0
        output[:,:,2]=0
    if mode=="g": #green is 1
        #green tint
        output[:,:,0]=0
        output[:,:,2]=0
    if mode=="r": #red is 2
        output[:,:,1]=0
        output[:,:,0]=0
    #bluring
    if mode=="x":#gausian blur
        ouput=cv2.GaussianBlur(frame,(15,15),0)
    if mode=="m":#median filter
        output=cv2.medianBlur(frame,15)
    #edge detection
    if mode=="s": #sobel edge detection
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
        sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
        output=cv2.magnitude(sobelx,sobely)
        output=np.uint8(output)
    if mode=="l":#laplacian
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        output=cv2.Laplacian(gray,cv2.CV_64F)
        output=np.uint8(np.absolute(output))
    if mode=="c":#canny
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        output=cv2.Canny(gray,100,200)
    #display the image
    cv2.imshow("Final result",output)
    keys=cv2.waitKey(1) & 0XFF
    if keys==ord("b"):
        mode="b"
    if keys==ord("g"):
        mode="g"
    if keys==ord("r"):
        mode="r"
    if keys==ord("c"):
        mode="c"
    if keys==ord("l"):
        mode="l"
    if keys==ord("s"):
        mode="s"
    if keys==ord("x"):
        mode="x"
    if keys==ord("m"):
        mode="m"
    if keys==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()