
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
def on_message(mqttc, userdata, msg):
    userdata['message_count'] += 1
    log.info(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}' with QoS {msg.qos}")
    if userdata['message_count'] >= userdata['maxmessages']:
        mqttc.loop_stop()


def eval_args():
    parser = argparse.ArgumentParser(description='Process MQTT host and wait time.')
    parser.add_argument('--mqtthost', type=str, default='172.24.0.1', help='MQTT host address')
    parser.add_argument('--maxmessages', type=int, default=60, help="number of messages before ending")
    parser.add_argument('--timeout', type=int, default=30, help="time in seconds before ending")
    return parser.parse_args()


def main():
    args = eval_args()
    userdata = {'message_count': 0, 'maxmessages': args.maxmessages}
    client.user_data_set(userdata)
    client.on_connect = on_connect
    client.on_message = on_message

    log.debug("before connect")
    client.connect(args.mqtthost, MQTT_PORT, 20)

    client.loop_start()
    log.debug("after connect")

    start_time = time.time()  # Record the start time
    while (time.time() - start_time) < args.timeout:
        time.sleep(1)

    client.disconnect()


if __name__ == '__main__':
    main()
    sys.exit()