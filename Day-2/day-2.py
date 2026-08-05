import cv2
img=cv2.imread(r"C:\Users\sanka\OneDrive\Documents\AI-PYTHON\Day-2\original.png")
greyImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original',img)
cv2.imshow('Gray',greyImage)
cv2.imwrite('GrayImage.jpg',greyImage)
