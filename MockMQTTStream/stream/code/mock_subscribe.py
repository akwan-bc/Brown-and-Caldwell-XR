
import argparse
import logging
import sys

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

MQTT_PORT = 1883
MQTT_TOPIC = 'mock'

# Define the MQTT client
client = mqtt.Client(CallbackAPIVersion.VERSION2, "mock_subscribe")

# Define the callback for when the client receives a CONNACK response from the server
def on_connect(mqttc, obj, flags, reason_code, properties):
    logging.info("Connected with result code "+str(reason_code))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mqttc.subscribe(MQTT_TOPIC, 0)

# Define the callback for when a PUBLISH message is received from the server
def on_message(mqttc, obj, msg):
    log.info(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}' with QoS {msg.qos}")

def eval_args():

    # Create the parser
    parser = argparse.ArgumentParser(description='Process MQTT host and wait time.')

    parser.add_argument('--mqtthost', type=str, default='172.24.0.1', help='MQTT host address')
    parser.add_argument('--waittime', type=int, default=1, help='Wait time in seconds')

    return parser.parse_args()


def main():

    args = eval_args()
    # Assign the callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT server
    client.connect(args.mqtthost, MQTT_PORT)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == '__main__':
    main()
    sys.exit()