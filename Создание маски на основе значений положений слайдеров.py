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

def get_slider_positions():
    H_up = cv2.getTrackbarPos('H_up', 'window_HSV')
    H_down = cv2.getTrackbarPos('H_down', 'window_HSV')
    S_up = cv2.getTrackbarPos('S_up', 'window_HSV')
    S_down = cv2.getTrackbarPos('S_down', 'window_HSV')
    V_up = cv2.getTrackbarPos('V_up', 'window_HSV')
    V_down = cv2.getTrackbarPos('V_down', 'window_HSV')
    return H_up, H_down, S_up, S_down, V_up, V_down
cap = cv2.VideoCapture(0)

create_window()

key = -1
while key == -1:
    isRead, image = cap.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    H_up, H_down, S_up, S_down, V_up, V_down = get_slider_positions()
    HSV_UP = [H_up, S_up, V_up]
    HSV_DOWN = [H_down, S_down, V_down]
    NP_HSV_UP = numpy.array(HSV_UP)
    NP_HSV_DOWN = numpy.array(HSV_DOWN)
    mask = cv2.inRange(image_hsv, NP_HSV_DOWN, NP_HSV_UP)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow('window_mask', mask)
    cv2.imshow('window', image)
    cv2.waitKey(20)

cap.release()