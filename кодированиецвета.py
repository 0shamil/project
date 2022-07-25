import cv2
image = cv2.imread('b.png')
print(image.shape)

print(image[0, 0], image[400, 400])

blue = image[600, 600]
green = image[600, 200]
red = image[200, 400]
print(blue, green, red)

yellow, cyan, magenta = image[300,300], image[600, 400], image[300,500]
print(yellow, magenta, cyan)

cv2.imshow('window', image)
cv2.waitKey()