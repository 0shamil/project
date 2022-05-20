# подключение функций и классов библиотек
from paho.mqtt.client import Client
payload_text = ''
from time import sleep
# функция обратного вызова, сообщаяющая результат подключения
def connect_status(device, userdata, flags, result):
    print('Устройство подключено с результатом', result)
# функция обратного вызова, сообщающая результат подписки
def subscribe_status(device, userdata, mid, qos):
    print('Устройство подписано', mid)
# функция обратного вызова для обработки сообщения
def receive_messages(device, userdata, message):
    global payload_text
    payload_text = message.payload.decode() # получение полезной нагрузки
    print(payload_text)
    device.publish('shm123/status', payload_text)
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
    device.publish('shm123/status', 'device on ' + str(i) + ' seconds' )
    i = i + 1
    sleep(1)
device.publish('shm123/status', 'device off')
device.loop_stop()