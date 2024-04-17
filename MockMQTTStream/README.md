# useful references

https://github.com/yakuza8/peniot/blob/fd1c644653a7d68d99fd2450090792704fbfd024/src/protocols/MQTT/examples/publisher_example.py

https://github.com/Matoussy/mqtt-kafka-bridge

https://opensource.com/article/18/6/mqtt


https://github.com/svet-b/grafana-mqtt-datasource?tab=readme-ov-file

https://pythonprogramming.net/live-graphs-data-visualization-application-dash-python-tutorial/

# Specific Steps

First bring up the docker containers
```shell
COMPOSE_DOCKER_CLI_BUILD=0 DOCKER_BUILDKIT=0 docker compose up
```

In a new terminal check existing containers are up
```shell
docker ps -a
```

Enter the mockmqttstream-mqtt-1 shell to get the mqtt host address
```shell
docker exec -it mockmqttstream-mqtt-1 sh
```

Once in the mockmqttstream-mqtt-1 shell the command to use is `ip route`.  The first line in the result is the mqtt host address
```
/ # ip route
default via 172.24.0.1 dev eth0 
172.24.0.0/16 dev eth0 scope link  src 172.24.0.3
```

In a separate terminal enter the stream shell
```shell
docker exec -it mockmqttstream-stream-1 bash
```

executing the run_mock.sh shell script will start publishing mock data to the mqtt broker and in parallel observing the data via a listener.  Example console logs are shown below.
```shell
root@a4c03dfec1ab:/opt/code# ./run_mock.sh 172.24.0.1 1 5 
2024-04-15 20:16:32,460 - INFO - mock_subscribe.py - 23 - Connected with result code Success
2024-04-15 20:16:32,750 - INFO - mock_publish.py - 32 - 172.24.0.1
2024-04-15 20:16:32,753 - INFO - mock_publish.py - 37 - Publishing to 172.24.0.1:1883 on topic 'mock'
2024-04-15 20:16:32,883 - INFO - mock_subscribe.py - 31 - Received message '{'timestamp_datetime': '2018-05-08 15:00:00', 'sensor_20': 58.59146999999999, 'sensor_21': 137.2398, 'sensor_23': 136.0752, 'sensor_25': 0.0}' on topic 'mock' with QoS 0
2024-04-15 20:16:33,884 - INFO - mock_publish.py - 51 - 0
2024-04-15 20:16:33,884 - INFO - mock_subscribe.py - 31 - Received message '{'timestamp_datetime': '2018-05-08 15:01:00', 'sensor_20': 58.59146999999999, 'sensor_21': 137.2398, 'sensor_23': 136.0752, 'sensor_25': 0.0}' on topic 'mock' with QoS 0
2024-04-15 20:16:34,885 - INFO - mock_publish.py - 51 - 1
2024-04-15 20:16:34,886 - INFO - mock_subscribe.py - 31 - Received message '{'timestamp_datetime': '2018-05-08 15:02:00', 'sensor_20': 59.40125, 'sensor_21': 137.8375, 'sensor_23': 134.6973, 'sensor_25': 0.0}' on topic 'mock' with QoS 0
2024-04-15 20:16:35,887 - INFO - mock_publish.py - 51 - 2
2024-04-15 20:16:35,889 - INFO - mock_subscribe.py - 31 - Received message '{'timestamp_datetime': '2018-05-08 15:03:00', 'sensor_20': 59.53545, 'sensor_21': 138.1248, 'sensor_23': 136.7632, 'sensor_25': 0.0}' on topic 'mock' with QoS 0
2024-04-15 20:16:36,890 - INFO - mock_publish.py - 51 - 3
2024-04-15 20:16:36,891 - INFO - mock_subscribe.py - 31 - Received message '{'timestamp_datetime': '2018-05-08 15:04:00', 'sensor_20': 62.01212, 'sensor_21': 138.4432, 'sensor_23': 134.6191, 'sensor_25': 0.0}' on topic 'mock' with QoS 0
2024-04-15 20:16:37,892 - INFO - mock_publish.py - 51 - 4
2024-04-15 20:16:38,894 - INFO - mock_publish.py - 51 - 5
2024-04-15 20:16:39,896 - INFO - mock_publish.py - 51 - 6
```




