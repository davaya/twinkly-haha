import paho.mqtt.client as mqtt
import os

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # Subscribe to everything (except control topics starting with $)
    client.subscribe('#')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f'{msg.topic} {str(msg.payload)}')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.tls_set()
user, pw, addr, port = os.getenv('MQTT_BROKER', '|||').split('|', maxsplit=3)
if not addr:
    print('No broker configured - setenv MQTT_BROKER user|pw|ip|port')
    exit(1)
print(f'Connecting to {user}@{addr}:{port}')
client.username_pw_set(user, pw)
client.connect(addr, int(port), 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
