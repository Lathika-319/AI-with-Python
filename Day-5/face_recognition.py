import cv2
alg="haarcascade_frontalface_default.xml"
Haar_cascade=cv2.CascadeClassifier(alg)#Load algorithm
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=Haar_cascade.detectMultiScale(grayImg,1.3,4) #detect multiple person->detectMultiScale
                                                      #1.3->resizing
                                                      #4->reduce false factor
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Face Detection",img)
    key=cv2.waitKey(10)
    if key==27: #Esc key
        break
cam.release()
cv2.destroyAllWindows()
