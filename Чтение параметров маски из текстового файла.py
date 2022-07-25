import cv2
import numpy


def read_values_from_file(filename):
    file = open('HSV.txt', 'r')
    values = file.read()
    print(values)
    values_split = values.split(',')
    print(values_split)
    for number in range(6):
        values_split[number] = int(values_split[number])
    print(values_split)
    file.close()
    return values_split

H_up, H_down, S_up, S_down, V_up, V_down = read_values_from_file('HSV.txt')

HSV_up = [H_up, S_up, V_up]
HSV_down = [H_down, S_down, V_down]
np_HSV_up = numpy.array(HSV_up)
np_HSV_down = numpy.array(HSV_down)





cap = cv2.VideoCapture(0)

key = -1

while key == -1:
    isRead, image = cap.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    mask = cv2.inRange(image_hsv, np_HSV_down, np_HSV_up)
    cv2.imshow('mask', mask)
    cv2.imshow('window', image)
    key = cv2.waitKey(20)
cap.release()