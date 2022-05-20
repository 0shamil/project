import cv2
cap = cv2.VideoCapture('robot.mp4')
for number in range(100):
    isRead, image = cap.read()
    cv2.circle(image, (480, 270), 50, (255, 0, 0), 3)
    cv2.circle(image, (480,270), 30, (0, 255, 0), -1)
    cv2.line(image, (480, 45), (480, 495), (255, 0, 255), 5)
    cv2.rectangle(image, (100,100), (850,430), (0, 255, 255), 5)
    cv2.imshow('window', image)
    cv2.waitKey(20)
cap.release()