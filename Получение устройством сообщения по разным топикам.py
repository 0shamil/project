from paho.mqtt.client import Client
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
def receive_room1(device, userdata, message):
    print('Первая комната', message.payload.decode())
def receive_room2(device, userdata, message):
    print('Вторая комната', message.payload.decode())
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.subscribe('shm123/room1')
device.subscribe('shm123/room2')
device.on_connect = connect_status
device.message_callback_add('shm123/room1', receive_room1)
device.message_callback_add('shm123/room2', receive_room2)
