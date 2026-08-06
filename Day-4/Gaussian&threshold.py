import cv2
img=cv2.imread(r"C:\Users\sanka\OneDrive\Documents\AI-PYTHON\Day-4\Original.jpg")

#destination=cv2.GaussianBlur(src,(kernal),borderType)

# gaussianImg=cv2.GaussianBlur(img,(41,41),50) -> more blurry
gaussianImg1=cv2.GaussianBlur(img,(21,21),0) #common practice

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresholdImg=cv2.threshold(img,180,255,cv2.THRESH_BINARY)[1]
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Gaussian Blur", gaussianImg1)
cv2.imshow("Threshold", thresholdImg)

cv2.imwrite("Original.jpg", img)
cv2.imwrite("Gray.jpg", gray)
cv2.imwrite("Gaussian.jpg", gaussianImg1)
cv2.imwrite("Threshold.jpg", thresholdImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
