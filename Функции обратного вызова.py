from paho.mqtt.client import Client
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)
device.on_connect = connect_status
device.loop_forever()