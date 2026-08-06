import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret:
        print("No frame")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
