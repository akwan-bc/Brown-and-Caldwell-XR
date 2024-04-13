#!/bin/bash

# Check if two arguments were provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <host_ip> <waittime> <maxiterations>"
    exit 1
fi

# Assign arguments to variables
HOST_IP=$1
NUMBER=${2:-1}
MAXITER=${3:-5}


# Execute the first Python script in the background and get its process ID
python3 mock_publish.py --mqtthost "$HOST_IP" --waittime "$NUMBER" --maxiter "$MAXITER" &
PID_SCRIPT1=$!

# Execute the second Python script in the background
python3 mock_subscribe.py --mqtthost "$HOST_IP" --maxmessages "$MAXITER" &

wait $PID_SCRIPT1