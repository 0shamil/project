import cv2
cap = cv2.VideoCapture('smart_car.mp4')

for number in range(200):
    isRead, image = cap.read()
    image[50, 550:750] = [0, 0, 255]
    image[50:250, 550] = [0, 0, 255]
    image[250, 550:750] = [0, 0, 255]
    image[50:250, 750] = [0, 0, 255]
    cv2.imshow('window', image)
    crop = image[50:250, 550:750]
    crop_resize = cv2.resize(crop, (200*2, 200*2))
    cv2.imshow('window_resize_crop', crop_resize)
    cv2.imshow('window_crop', crop)
    zone1 = image[0:360, 0:640]
    zone2 = image[360:720, 0:640]
    zone3 = image[0:360, 640:1280]
    zone4 = image[360:720,640:1280]
    cv2.imshow('window_zone1', zone1)
    cv2.imshow('window_zone2', zone2)
    cv2.imshow('window_zone3', zone3)
    cv2.imshow('window_zone4', zone4)
    cv2.waitKey(20)

print(image.shape)
cap.release()
