import cv2
import numpy


def create_window():
    cv2.namedWindow('window_HSV')
    cv2.resizeWindow('window_HSV', 400, 350)
    cv2.createTrackbar('H_up', 'window_HSV', 255, 255, print)
    cv2.createTrackbar('H_down', 'window_HSV', 0, 255, print)
    cv2.createTrackbar('S_up', 'window_HSV', 255, 255, print)
    cv2.createTrackbar('S_down', 'window_HSV', 0, 255, print)
    cv2.createTrackbar('V_up', 'window_HSV', 255, 255, print)
    cv2.createTrackbar('V_down', 'window_HSV', 0, 255, print)

cap = cv2.VideoCapture(0)

create_window()
h_up, s_up, v_up = 140, 255, 255
h_down, s_down, v_down = 120, 50, 50
HSV_UP = [h_up, s_up, v_up]
HSV_DOWN = [h_down, s_down, v_down]
NP_HSV_UP = numpy.array(HSV_UP)
NP_HSV_DOWN = numpy.array(HSV_DOWN)

key = -1
while key == -1:
    isRead, image = cap.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    mask = cv2.inRange(image_hsv, NP_HSV_DOWN, NP_HSV_UP)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow('window_mask', mask)
    cv2.imshow('window', image)
    cv2.waitKey(20)

cap.release()