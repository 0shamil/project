import cv2
image = cv2.imread('a.jpeg')
print(image.shape)
print(image[0, 0])
print(image[599, 1149])
cv2.imshow('window', image)
cv2.waitKey()