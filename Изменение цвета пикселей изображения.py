import cv2
image = cv2.imread('c.jpeg')
print(image.shape)

image[50, 100] = [0, 0, 255]
image[50, 101] = [0, 0, 255]
image[50, 99] = [0, 0, 255]
image[50, 100:300] = [0, 0, 255]
image[50:250, 100] = [0, 0, 255]
image[250, 100:300] = [0, 0, 255]
image[50:250, 300] = [0, 0, 255]

cv2.imshow('window', image)
cv2.waitKey()
