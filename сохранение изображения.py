import cv2
image = cv2.imread('g.png')
height, width, service = image.shape

print (height, width)
for i in range(0, height, 76):
    image[i, 0:width] = [0, 255, 255]
for i in range(0, width, 60):
    image[0:height, i] = [0, 255, 255]
crop = image[456:533, 720:780]
cv2.imshow('window_crop', crop)
crop_height, crop_width, crop_service = crop.shape
crop_resize = cv2.resize(crop, (crop_width*5, crop_height*5))
cv2.imshow('window_crop_resize', crop_resize)
cv2.imshow('window', image)
cv2.waitKey()
cv2.imwrite('g.png', crop_resize)