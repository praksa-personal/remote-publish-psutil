import random
from paho.mqtt import client as mqtt_client
from collect_data import allData
from time import sleep

broker = '10.30.10.47'
port = 1883
topic = "emqx/remote"
# generate client ID with pub prefix randomly
this_client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'Remote_user_456'
password = '1234'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id=this_client_id, clean_session=True)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    client.subscribe(topic)
    client.on_message = on_message


def publish(client, topic, user, msg):
    fmsg = user + ": " + msg
    result = client.publish(topic, fmsg, qos=1)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    return fmsg

if __name__ == '__main__':
    client = connect_mqtt()
    while(1):
        msg = allData()
        publish(client,"emqx/remote",username,msg)
        sleep(10)
