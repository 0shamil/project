from paho.mqtt.client import Client
import numpy as np

def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
def subscribe_status(device, userdata, mid, qos):
    print('Устройство подписано', mid)

def receive_room1(device, userdata, message):
    pt1 = message.payload.decode
    print('Первая комната', pt1)
    arr = np.random.randint(pt1, pt2, 1)
    print(arr)

def receive_room2(device, userdata, message):
    pt2 = message.payload.decode
    print('Вторая комната', pt2)
    arr = np.random.randint(pt1, pt2, 1)
    print(arr)
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.subscribe('shm123/room1')
device.subscribe('shm123/room2')
device.on_connect = connect_status
device.message_callback_add('shm123/room1', receive_room2)
device.message_callback_add('shm123/room2', receive_room1)
device.loop_forever()