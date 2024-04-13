# Getting set up

## Build & run the container
1.  At the `MockSensorData` folder, run `docker-compose build`
2.  Once above is complete, run `docker-compose run`
3.  Once above is complete, in a separate terminal run `docker exec -it [container name] bash`

## Run jupyter lab inside the container
1.  Inside the container, run `jupyter lab --ip=0.0.0.0 --port=8080 --no-browser`
2.  In a browser, open up `http://127.0.0.1:8080/lab?token=[token value]`

## Useful commands
