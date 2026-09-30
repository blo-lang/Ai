import cv2
import mediapipe as mp
import math
from pycaw.pycaw import AudioUtilities #control the volume
import screen_brightness_control as sbc #screen brightness
#turn on webcam
cam=cv2.VideoCapture(0)
#setup mediapipe
mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils
hands=mp_hands.Hands(min_detection_confidence=0.50,min_tracking_confidence=0.5)
#access computer speakers
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
#program loop
while True:
    success, frame = cam.read()
    if not success:
        print("Error: Cannot read cam")
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #detect hands
    result=hands.process(rgb)
    if result.multi_hand_landmarks:
        #check each hand landmark
        for hand,handedness in zip(result.multi_hand_landmarks,result.multi_handedness):
            #draw the hand connections
            mp_draw.draw_landmarks(frame,hand,mp_hands.HAND_CONNECTIONS)
            #get the finger indexes
            thumb=hand.landmark[4]
            index=hand.landmark[8]
            h,w,c=frame.shape
            #convert the landmark positions into pixels
            x1=int(thumb.x*w)
            y1=int(thumb.y*h)
            x2=int(index.x*w)
            y2=int(index.y*h)
            #calculate the distance between fingers
            distance=math.hypot(x2-x1,y2-y1)
            #ranges between 0 and 100
            level=int(min(max((distance)/150*100,0),100))
            #identify the hand
            hand_name=handedness.classification[0].label
            #right=volume
            if hand_name=="Right":
                volume.SetMasterVolumeLevelScalar(level/100,None)
                cv2.putText(frame,f"Right hand volume:{level}%",(30,50),cv2.FONT_)