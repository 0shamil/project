import cv2
from paho.mqtt.subscribe import simple

fl = cv2.imread('flower.jpeg')
car = cv2.imread('cars.jpeg')
cow = cv2.imread('cow.jpeg')

message = simple('shm123/message',
       hostname='mqtt.pi40.ru',
       port=1883,
       client_id='python_qw21',
       auth={'username': 'shm123', 'password': 'asd1asd'})

print(message.payload.decode())
m = message.payload.decode()

if m == 'flower.jpeg':
    cv2.imshow('window', fl)

if m == 'cars.jpeg':
    cv2.imshow('window', car)

if m == 'cow.jpeg':
    cv2.imshow('window', cow)


cv2.waitKey()