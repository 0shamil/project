import cv2
cap = cv2.VideoCapture('car_move.mp4')

for number in range(350):
    isRead, image = cap.read()
    cv2.imshow('window', image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('window_gray', image_gray)
    print(image_gray[270, 480])
    value_threshold, image_threshold = cv2.threshold(image_gray, 200, 255,
                                                     cv2.THRESH_BINARY)
    cv2.imshow('window_threshold', image_threshold)
    cv2.waitKey(30)
cap.release()