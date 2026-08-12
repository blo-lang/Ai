import cv2 #opencv-used for image processing
#load the image
img=cv2.imread("earth.png")#imread is used to read the image
#convert the image to black and white
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#display the grayscale(black and white) image
cv2.imshow("Grayscale image",gray)
#create a resizeable window
cv2.namedWindow("Resizeable window",cv2.WINDOW_NORMAL) #WINDOW_NORMAL is used to allow the window to be resizeable
#set the height and the width of the window
cv2.resizeWindow("Resizeable window",800,500)
#display the read image
cv2.imshow("A random Image",img)#imshow is used to show an image
#when displaying images you need to start with the title
#keep the window open
cv2.waitKey(0)#0 is the index for the close button
#when user clicks the x release the window
cv2.destroyAllWindows()
