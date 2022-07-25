import cv2

cap = VideoCapture(0)

key = -1
while key == -1:
    isRead, image = cap.read()
    pixel = image[480, 120]
    print(pixel)
    blue, green, red = pixel
    cv2.line(image, (0,240), (639,240), (255, 0, 0), 5)
    cv2.line(image, (320, 0), (320, 479), (255, 0, 0), 5)

    cv2.circle(image, (480, 120), 30, (int(blue), int(green), int(red)), -1)
    cv2.circle(image, (480, 360), 30, (int(blue), int(green), int(red)), -1)
    cv2.circle(image, (160, 360), 30, (int(blue), int(green), int(red)), -1)
    cv2.circle(image, (160, 120), 30, (int(blue), int(green), int(red)), -1)

    cv2.imshow('window', image)
    key = cv2.waitKey(30)
    print(key)

cap.release()