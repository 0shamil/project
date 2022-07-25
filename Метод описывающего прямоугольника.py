import cv2

cap = cv2.VideoCapture('car_move.mp4')
for number in range(350):
    isRead, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    value, mask = cv2.threshold(image_gray, 240, 255, cv2.THRESH_BINARY)
    contours, service = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
    for c in contours:
        x, y, width, height = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)
    cv2.imshow('window', image)
    cv2.waitKey(20)

cap.release()