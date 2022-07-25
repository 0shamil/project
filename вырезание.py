import cv2
image = cv2.imread('e.jpeg')
print(image.shape)

image[440:600, 400:610] = [255, 0, 0] #закраска

crop = image[150:250, 650:800] #выделение области для вырезания

cv2.imshow('window_crop', crop) #вывод на экран обрезаной области
cv2.imshow('window', image)
cv2.waitKey()
