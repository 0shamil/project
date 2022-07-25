import cv2

cap = cv2.VideoCapture(0)

key = -1
while key == -1:
    isRead, image = cap.read()
    cv2.imshow('window', image)
    key = cv2.waitKey(30)

cap.release()