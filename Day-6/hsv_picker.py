import cv2

def nothing(x):
    pass

cam = cv2.VideoCapture(0)

cv2.namedWindow("HSV Trackbars")

# Hue
cv2.createTrackbar("H Low", "HSV Trackbars", 0, 179, nothing)
cv2.createTrackbar("H High", "HSV Trackbars", 179, 179, nothing)

# Saturation
cv2.createTrackbar("S Low", "HSV Trackbars", 0, 255, nothing)
cv2.createTrackbar("S High", "HSV Trackbars", 255, 255, nothing)

# Value
cv2.createTrackbar("V Low", "HSV Trackbars", 0, 255, nothing)
cv2.createTrackbar("V High", "HSV Trackbars", 255, 255, nothing)

while True:

    _, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get slider values
    hLow = cv2.getTrackbarPos("H Low", "HSV Trackbars")
    hHigh = cv2.getTrackbarPos("H High", "HSV Trackbars")

    sLow = cv2.getTrackbarPos("S Low", "HSV Trackbars")
    sHigh = cv2.getTrackbarPos("S High", "HSV Trackbars")

    vLow = cv2.getTrackbarPos("V Low", "HSV Trackbars")
    vHigh = cv2.getTrackbarPos("V High", "HSV Trackbars")

    lower = (hLow, sLow, vLow)
    upper = (hHigh, sHigh, vHigh)

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("Camera", frame)
    cv2.imshow("Mask", mask)

    print("Lower:", lower, "Upper:", upper)

    key = cv2.waitKey(1)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
