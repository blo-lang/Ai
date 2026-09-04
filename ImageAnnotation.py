import cv2
img=cv2.imread("earth.png")
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#add text to the image
cv2.putText(rgb,"Annotated Image",(10,30),cv2.FONT_ITALIC,1,(0,220,200),2)
#draw a rectangle
cv2.rectangle(img,(100,200),(200,200),(255,255,255),5)
#outlined circle
cv2.circle(img,(400,200),50,(0,255,0),2)
#filled circle
cv2.circle(img,(200,400),50,(255,0,0),-1)
#draw a line
cv2.line(img,(100,400),(500,400),(255,0,0),3)
#arrowed line
cv2.arrowedLine(img,(50,300),(50,600),(0,0,255),6)
#keep the windowopen
cv2.imshow("Annotated Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()