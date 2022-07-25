from paho.mqtt.publish import single
import cv2

image = cv2.imread('cars.jpeg')
h, w, c = image.shape
print()

single('shm123/one_message',
       payload=str(w)+', '+str(h)+',' +str(c),
       hostname='mqtt.pi40.ru',
       port=1883,
       client_id='python_qw21',
       auth={'username': 'shm123', 'password': 'asd1asd'})
