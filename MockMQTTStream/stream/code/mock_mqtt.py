import paho.mqtt.client as mqtt
from time import sleep
import socket
import ipaddress
import psutil

from paho.mqtt.enums import CallbackAPIVersion
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

MQTT_PORT = 1883
MQTT_TOPIC = 'ping'

def main():
    host_ip = socket.gethostbyname(socket.gethostname())
    log.info(host_ip)
    #this_ip_network = ipaddress.ip_network(host_ip)
    #log.info(this_ip_network)
    #all_hosts = list(ipaddress.ip_network(host_ip).hosts())
    #client_ip = socket.getnameinfo()
    #log.info(all_hosts)
    connections = psutil.net_connections()
    
    log.info(connections)
    log.info(str(MQTT_PORT))
    i = 0
    mqtt_port = ""
    for c in connections:
        #conn_raddr = c.raddr
        #log.info(c)
        if c.raddr != ():
            log.info(c.raddr)
            log.info(str(MQTT_PORT))
            if c.raddr.port == str(MQTT_PORT):
                mqtt_port = c.raddr.port
                log.info(mqtt_port)
        i += 1

    client = mqtt.Client(CallbackAPIVersion.VERSION2, "mock_mqtt")
    client.connect(host="172.24.0.1", port=MQTT_PORT)
    client.loop_start()

    log.info(f"Publishing to 172.24.0.1:{MQTT_PORT} on topic '{MQTT_TOPIC}'")

    iterations = 5
    for i in range(iterations):

        str_val = str(i)
        log.info(str_val)
        
        r = client.publish(
            topic=MQTT_TOPIC,
            payload=bytes(str_val, 'utf-8')
        )
        r.wait_for_publish()
        sleep(1)


if __name__ == '__main__':
    main()
    sys.exit()