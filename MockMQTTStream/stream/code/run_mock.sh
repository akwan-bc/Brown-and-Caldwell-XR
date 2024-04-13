#!/bin/bash

# Check if two arguments were provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <host_ip> <number>"
    exit 1
fi

# Assign arguments to variables
HOST_IP=$1
NUMBER=$2

# Execute the first Python script in the background and get its process ID
python3 mock_publish.py --mqtthost "$HOST_IP" --waittime "$NUMBER" &
#PID_SCRIPT1=$!

# Execute the second Python script in the background
python3 mock_subscribe.py -mqtthost "$HOST_IP" --waittime 1 &

# Wait only for the first script to finish
wait #$PID_SCRIPT1
