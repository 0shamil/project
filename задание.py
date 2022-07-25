from paho.mqtt.client import Client
import cv2
cap = cv2.VideoCapture(0)
for number in range(200):
    isRead, image = cap.read()
    cv2.imshow('window', image)
    cv2.waitKey(30)
cap.release()
print(image.shape)
h, w, c = image.shape
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
def subscribe_status(device, userdata, mid, qos):
    print('Устройство подписано', mid)
def receive_messages(device, userdata, message):
    payload_text = 'weight = ' + str(w) + ' ' + 'height = ' + str(h)
    print(payload_text)
    device.publish('shm123/task', payload_text)
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.on_connect = connect_status
device.subscribe('shm123/switch')
device.on_subscribe = subscribe_status
device.on_message = receive_messages
device.loop_forever()