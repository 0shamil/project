import cv2

cap = cv2.VideoCapture(0)

def find_center(x, y, width, height, image):
    x_center = x + width//2
    y_center = y + height//2
    cv2.circle(image, (x_center, y_center), 10, (0, 0, 255), -1)
    detect_zone(x_center, y_center, image)

def detect_zone(x_center, y_center, image):
    if x_center <= 213:
        cv2.putText(image, 'left', (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    elif x_center >= 426:
        cv2.putText(image, 'right', (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    else:
        cv2.putText(image, 'middle', (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
key = -1
while key == -1:
    isRead, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.blur(image_gray, (5, 5))
    value, mask = cv2.threshold(gray_blur, 230, 255, cv2.THRESH_BINARY)
    cv2.imshow('window_mask', mask)
    contours, service = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
    cv2.line(image, (213, 0), (213, 479), (255, 0, 0), 5)
    cv2.line(image, (426, 0), (426, 479), (255, 0, 0), 5)

    for c in contours:
        x, y, width, height = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)
        find_center(x, y, width, height, image)

    cv2.imshow('window', image)
    key = cv2.waitKey(20)

cap.release()