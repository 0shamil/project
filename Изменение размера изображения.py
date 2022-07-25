import cv2

image = cv2.imread('f.jpeg')
print(image.shape)
cv2.imshow('window', image)
cv2.imshow('window2', cv2.resize(image, (750*2, 500*2)))

height, width, service = image.shape
image_resize = cv2.resize(image, (width*2, height*2))
cv2.imshow('window3', image_resize)

image_resize_small = cv2.resize(image, (int(width*0.5), int(height*0.5)))
cv2.imshow('window4', image_resize_small)
cv2.waitKey()
