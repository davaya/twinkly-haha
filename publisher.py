import paho.mqtt.publish as publish
import os

PREFIX = 'DaveK'

user, pw, host, port = os.getenv('MQTT_BROKER', '|||').split('|', maxsplit=3)
if not host:
    print('No broker configured - setenv MQTT_BROKER user|pw|host|port')
    exit(1)
print(f'Publishing to {user}@{host}:{port} on channel {PREFIX}/*')
login = {'username': user, 'password': pw}

query_features = {
    "action": "query",
    "target": {
        "features": []
    },
    "args": {
        "response_requested": "complete"
    }
}

publish.single(PREFIX + "/oc2/cmd", payload=str(query_features), qos=0, retain=False, hostname=host,
    port=int(port), client_id="", keepalive=60, will=None, auth=login, tls=None)
