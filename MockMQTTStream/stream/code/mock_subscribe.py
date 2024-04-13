
import argparse
import logging
import sys
import time

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion


logging.basicConfig(stream=sys.stdout, level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')
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
    global message_count
    log.info(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}' with QoS {msg.qos}")
    message_count += 1


def eval_args():

    # Create the parser
    parser = argparse.ArgumentParser(description='Process MQTT host and wait time.')

    parser.add_argument('--mqtthost', type=str, default='172.24.0.1', help='MQTT host address')
    parser.add_argument('--maxmessages', type=int, default=60, help="number of messages before ending")

    return parser.parse_args()


def main():

    args = eval_args()
    # Assign the callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    log.debug("before connect")
    # Connect to the MQTT server
    client.connect(args.mqtthost, MQTT_PORT, 20)

    client.loop_start()
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    log.debug("after connect")

    # Wait for the specified time or until the message count is reached
    while message_count < args.maxmessages:
        time.sleep(1)

    # Stop the loop and disconnect
    client.loop_stop()
    client.disconnect()


if __name__ == '__main__':
    main()
    sys.exit()