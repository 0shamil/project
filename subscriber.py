from paho.mqtt.subscribe import simple

message = simple('shm123/message',
       hostname='mqtt.pi40.ru',
       port=1883,
       client_id='python_qw21',
       auth={'username': 'shm123', 'password': 'asd1asd'})

print(message.payload.decode())