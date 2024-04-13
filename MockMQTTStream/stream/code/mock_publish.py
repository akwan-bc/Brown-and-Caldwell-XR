import argparse
import logging
import sys
from time import sleep

import pandas as pd
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

logging.basicConfig(stream=sys.stdout, level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')
log = logging.getLogger(__name__)

MQTT_PORT = 1883
MQTT_TOPIC = 'mock'

def eval_args():

    # Create the parser,
    parser = argparse.ArgumentParser(description='Process MQTT host and wait time.')

    parser.add_argument('--mqtthost', type=str, default='172.24.0.1', help='MQTT host address')
    parser.add_argument('--waittime', type=int, default=1, help='Wait time in seconds')
    parser.add_argument('--maxiter', type=int, default=5, help="Max iterations")

    return parser.parse_args()

def main():

    args = eval_args()
    host_ip = args.mqtthost
    log.info(host_ip)
    
    client = mqtt.Client(CallbackAPIVersion.VERSION2, "mock_publish")
    client.connect(host=host_ip, port=MQTT_PORT)
    client.loop_start()
    log.info(f"Publishing to {host_ip}:{MQTT_PORT} on topic '{MQTT_TOPIC}'")

    mock_df = pd.read_excel('mqtt_mock_data.xlsx', usecols=lambda column: column not in ['Unnamed: 0'])
    mock_df['timestamp_datetime'] = mock_df['timestamp_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    for index, row in mock_df.iterrows():
        row_data = row.to_dict()
        log.debug(str(row_data))
        
        r = client.publish(
            topic=MQTT_TOPIC,
            payload=bytes(str(row_data), 'utf-8')
        )
        r.wait_for_publish()
        sleep(args.waittime)
        log.info(index)
        if index > args.maxiter:
            break


if __name__ == '__main__':
    main()
    sys.exit()