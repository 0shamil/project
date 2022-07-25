import cv2
import numpy

cap = cv2.VideoCapture('blue_car.mp4')

h_up, s_up, v_up = 140, 255, 255
h_down, s_down, v_down = 120, 70, 70

HSV_UP = [h_up, s_up, v_up]
HSV_DOWN = [h_down, s_down, v_down]

NP_HSV_UP = numpy.array(HSV_UP)
NP_HSV_DOWN = numpy.array(HSV_DOWN)

for number in range(330):
    isRead, image = cap.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    mask = cv2.inRange(image_hsv, NP_HSV_DOWN, NP_HSV_UP)
    cv2.imshow('window_mask', mask)
    cv2.imshow('window', image)
    cv2.waitKey(20)

cap.release()
