import cv2 #webcam processing
import mediapipe as mp #gesture detection
import pyautogui #scrolling
import time #detect delay during scrolling
#setup mediapipe
mp_hands=mp.solutions.hands
#hand detector
hands=mp_hands.Hands(max_num_hands=1)
mp_draw=mp.solutions.drawing_utils
#turn on webcam
cam=cv2.VideoCapture(0)
prev_y=None #previous positions of the finger
while True:
    #read cam
    success,frame=cam.read()
    if not success:
        print("Error:could not read cam")
        break
    frame-cv2.flip(frame,1)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)
    if result.multi_hand_landmarks:
        #get detected hand
        hand=result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
        ##get index finger
        finger=hand.landmark[0]
        h,w_=frame.shapre
        y=int(finger.y*h)
        if prev_y is not None:
            movement=y-prev_y
            #finger up
            if movement>8:
                pyautogui.scroll(-5)
            elif movement<-8:
                pyautogui.scroll(5)
        #save the finger position
        prev_y=y
    else:
        prev_y=None
    cv2.imshow("Scrolling using gestures",frame)
    cv2.waitkey(1)
cam.release()
cv2.destroyAllWindows()