import imutils
import cv2

redLower=(10,95,116) #(hue,saturation,value)
redUpper=(102,248,194)

cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    frame=imutils.resize(frame,width=500)
    blurred=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    
    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)   #Remove tiny unwanted parts
    mask=cv2.dilate(mask,None,iterations=2)  #Make the detected object stronger/solid

    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2] #find contour/things
    center=None

    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c) #Find center and radius
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"])) #calculating for Find exact center
        if radius>10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2) #drawing circle
            cv2.circle(frame,center,5,(0,0,255),-1) #drawing center of circle
            print(center,radius)
            if radius>250:
                print("Stop")
            else:
                if(center[0]<150):
                    print("Right")
                elif (center[0]>450):
                    print("Left")
                elif(radius<250):
                    print("Front")
        cv2.imshow("Color Detection", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
    
