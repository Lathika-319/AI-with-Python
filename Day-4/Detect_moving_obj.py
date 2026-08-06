import cv2
import imutils  #resizing

cam=cv2.VideoCapture(0) #Open the default webcam.
#cv2.VideoCapture("video.mp4")

firstFrame=None #initalizing first frame as none
area=2000 #ininitalizing area and required to consider an object as moving

while True: # Infinite loop to continuously capture video frames
    a,img=cam.read() #that video is saved in img
                     #o/p-> True, image
    
    text="Normal" # Default status displayed on the video frame
    
    img=imutils.resize(img,width=1000) #resizing the window
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #coverting color video to grey
    gaussianImg=cv2.GaussianBlur(grayImg,(21,21),0) #camera contains tiny noise.Blur removes noise.

    if firstFrame is None:
        firstFrame=gaussianImg #assign gaussainImg to firstFrame
        continue #we'r not going to compare with firstFrame
    
    imgDiff=cv2.absdiff(firstFrame,gaussianImg)
    #cv2.absdiff(src1, src2)
    #Absolute Difference between two images.
    
    threshImg=cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1] #applying threshold ,threshold_value=25 and max_value=255 [0-25->black and 25-255->white] and "[1]"->if its 0 ,then only value is returned .not as image

    threshImg=cv2.dilate(threshImg,None,iterations=2)#Threshold creates tiny gaps.Dilation fills them.Now the moving object becomes solid object.
                                                     #Expand twice.->iterations=2
    
    cnts=cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #contour ->Boundary of an object.
    #findContours-> Find every object's outline
    #threshImg.copy()-> OpenCV may modify the image internally.So we pass a copy.
    #cv2.RETR_EXTERNAL ->Find only the outer contour.Ignore contours inside.
    #cv2.CHAIN_APPROX_SIMPLE-> Instead of storing every point.it stores only necessary points.(Store only corner points)
    
    cnts=imutils.grab_contours(cnts)#save everyframe into cnts
    #grab_contours() gives you just the contour list,
    
    for c in cnts:
        if cv2.contourArea(c)<area: #allows only ,if area is above 500
            continue
        (x,y,w,h)=cv2.boundingRect(c) #creating rectangle box around contour
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Moving object detected" #with tab name
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)#text type
    cv2.imshow("CameraFeed:",img) #display the o/p
    key=cv2.waitKey(1) #wait for 10sec
        #print(key)
    if key==ord("q"): #to exists press "q"
        break
cam.release()
cv2.destroyAllWindows()
