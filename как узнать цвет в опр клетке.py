import cv2
from paho.mqtt.publish import single

image = cv2.imread('cars.jpeg')
r, g, b = image[0, 0]

single('shm123/one_message',
       payload=str(r)+','+str(g)+','+ str(b),
       hostname='mqtt.pi40.ru',
       port=1883,
       client_id='python_qw21',
       auth={'username': 'shm123', 'password': 'asd1asd'})