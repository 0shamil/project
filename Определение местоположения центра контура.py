import cv2

cap = cv2.VideoCapture(0)

key = -1
while key == -1:
    isRead, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.blur(image_gray, (5, 5))
    value, mask = cv2.threshold(gray_blur, 230, 255, cv2.THRESH_BINARY)
    cv2.imshow('window_mask', mask)
    contours, service = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
    if contours != []:
        c = contours[0]
        x, y, width, height = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)

    cv2.imshow('window', image)
    key = cv2.waitKey(20)

cap.release()