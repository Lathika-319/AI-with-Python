from facial_emotion_recognition import EmotionRecognition
import cv2
er=EmotionRecognition(device='cpu')
image_path = r"C:\Users\sanka\OneDrive\Documents\AI-PYTHON\Day-7\input.jpeg"
cam=cv2.imread(image_path)
frames=er.recognise_emotion(cam,return_type='BGR') #words color
cv2.imshow("Frame",frames)
key=cv2.waitKey(1)
cam.release()
cv2.destroyAllWindows()
    
''''By using Live video
from facial_emotion_recognition import EmotionRecognition
import cv2
er=EmotionRecognition(device='cpu')
cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    frames=er.recognize_emotion(frame,return_type='BGR') #words color
    cv2.imshow("Frame",frames)
    key=cv2.waitKey(1)
    if key==27: #only for many frames to exist from camera
        break
cam.release()
cv2.destroyAllWindows()'''
    
