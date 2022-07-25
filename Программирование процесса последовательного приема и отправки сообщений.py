from paho.mqtt.client import Client
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
def subscribe_status(device, userdata, mid, qos):
    print('Устройство подписано', mid)
def receive_messages(device, userdata, message):
    payload_text = message.payload.decode()
    print(payload_text)
    device.publish('shm123/input', payload_text)
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.subscribe('shm123/switch')
device.on_connect = connect_status
device.on_subscribe = subscribe_status
device.on_message = receive_messages
device.loop_forever()