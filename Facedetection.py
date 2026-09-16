import cv2
#load the pretrained model
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#turn on your webcam
cam=cv2.VideoCapture(0)
if not cam.isOpened():
    #opencv could not access camera
    print("Error: Could not access camera")
    exit()
while True: #as long as the cam is on
    #rease the image in the cam
    success,frame=cam.read()
    if not success:
        #opencv could not process your image
        print("Error:Could not read image")
        break
    #convert the frames to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect faces on the gray image
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    #draw a rectangle around detected faces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    #display the output
    cv2.imshow("Face Detecting",frame)
    #keep the winow open
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
#release the webcam
cam.release()
cv2.destroyAllWindows()