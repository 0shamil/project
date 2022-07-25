from paho.mqtt.client import Client
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
def subscribe_status(device, userdata, mid, qos):
    print('Устройство подписано', mid)
def receive_messages(device, userdata, message):
    print(message.payload.decode())
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.on_connect = connect_status
device.subscribe('shm123/task')
device.on_subscribe = subscribe_status
device.on_message = receive_messages
device.loop_forever()