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


