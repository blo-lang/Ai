import cv2
import mediapipe as mp
#initialize mediapipe
mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils#outline your hand
#hand detector
hands=mp_hands.Hands(max_num_hands=2)
#open the webcam
cam=cv2.VideoCapture(0)
while True:
    success,frame=cam.read()
    if not success:
        print("Error: couldn not access the webcam")
        break
    #flip the image
    frame=cv2.flip(frame,1)
    #convert to rgb
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #detect the hand
    result=hands.process(rgb)#process means understand/detect
    #check is hand landmarks were registered
    if result.multi_hand_landmarks:
        #check each landmark
        for landmark in result.multi_hand_landmarks:
            #draw an out like
            mp_draw.draw.landmarks(frame,landmark,mp_hands.HAND_CONNECTIONS)
        #display the output
        cv2.imshow("Detected Hand",frame)
        #q-quit
        if cv2.waitKey(1) & 0XFF==ord("q"):
            break
cam.release()
cv2.destroyAllWindows()