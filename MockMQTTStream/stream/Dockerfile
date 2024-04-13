FROM ubuntu:22.04

WORKDIR /opt/code/

RUN apt-get -y update && apt-get -y install gcc libpq-dev libevent-dev pspg python3-pip
# Install dependencies
COPY requirements.txt .
# Install dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["/bin/bash"]