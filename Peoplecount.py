import cv2
#load the classifier
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#turn on the webcam
cam=cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error:Cam not found")
    exit()
while True:
    #capture frame by frame
    success,frame=cam.read()
    if not success:
        print("Error: Video Capture failed")
        break
    #convert the frames to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect the faces
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    #draw rectangles around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),5)
        #people count
        font=cv2.FONT_ITALIC
        cv2.putText(frame,f"People's Count:{len(faces)}",(10,30),font,1,(255,255,255),2)
        #display the output
        cv2.imshow("Face Tracking and Face Count",frame)
        #keep the window open
        if cv2.waitKey(1)&0XFF==ord("c"):
            break
cam.release()
cv2.destroyAllWindows()