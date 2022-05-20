from paho.mqtt.client import Client
from time import sleep
device = Client('python_qw21')
device.username_pw_set('shm123', 'asd1asd')
device.connect('mqtt.pi40.ru', 1883)

i = 0
while i < 10:
    device.publish('shm123/number', i)
    sleep(2)
    i = i + 1