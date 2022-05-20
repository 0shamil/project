from paho.mqtt.client import Client
from time import sleep
import cv2
cap = cv2.VideoCapture(0)
for number in range(200):
    isRead, image = cap.read()
    cv2.imshow('window', image)
    cv2.waitKey(30)
cap.release()
print(image.shape)
h, w, c = image.shape
payload_text = ''
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
def subscribe_status(device, userdata, mid, qos):
    print('Устройство подписано', mid)
def receive_messages(device, userdata, message):
    payload_text = message.payload.decode()
    print(payload_text)
    device.publish('shm123/qqq', payload_text)
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.subscribe('shm123/switch')
device.on_connect = connect_status
device.on_subscribe = subscribe_status
device.on_message = receive_messages
device.loop_start()
i = 0
while payload_text != '1':
    device.publish('shm123/task', )
    i = i + 1
    sleep(1)
device.publish('shm123/task', str(w) + str(h))
device.loop_stop()