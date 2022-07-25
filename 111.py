import cv2
from paho.mqtt.subscribe import simp

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

if m == '1':
       cv2.imshow('window', fl)

if m == '2':
       cv2.imshow('window', car)

if m == '3':
       cv2.imshow('window', cow)

cv2.waiKey()