import cv2
image = cv2.imread('d.jpeg')

for i in range(0, 600, 50):
    image[i, 0:900] = [0, 0, 255]
for i in range(0, 900, 50): #цикл
    image[0:600, i] = [0, 0, 255]

cv2.imshow('window', image)
print(image.shape)
cv2.waitKey()