import cv2

image = cv2.imread('road.jpeg')
print(image)
cv2.imshow('window',image)
cv2.waitKey()