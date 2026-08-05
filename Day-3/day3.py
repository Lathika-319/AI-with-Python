'''import cv2
print(cv2.__version__)'''

import cv2  #importing
img=cv2.imread(r"C:\Users\sanka\OneDrive\Documents\AI-PYTHON\Day-3\input_image.png") #extension is mandatory
cv2.imshow('show',img)       #Display the image in a window named 'show'
cv2.imwrite('output_image.jpg',img) #copying img
cv2.waitKey(10000)           #Wait for 10000 milliseconds (10 seconds)
#cv2.waitKey(500)
cv2.destroyAllWindows()      #closing window

