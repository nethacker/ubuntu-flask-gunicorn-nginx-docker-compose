# ubuntu-flask-gunicorn-nginx-docker-compose
Scaled Python Flask App with NGINX using Multiple Containers with Docker Compose

## Contents
- Ubuntu 18.04
- Python 3.7.3
- Flask 1.0.3
- NGINX 1.17.1
- Werkzeug 0.15.4
- Gunicorn 19.9.0
- Example "Hello World" Flask App

## Build and start your containers with Docker Compose
Run this command in the directory that has your docker-compose.yml
```
docker-compose up --build --detach
```

## Testing
If you didn't modify the example code you should be able to go to localhost port 80 in a browser and get a red "Hello World" message

## Notes
- --shm-size is to set a bigger shared memory size. Gunicorn has a config entry to use shared memory (/dev/shm) vs disk (/tmp) for health checks to avoid timeouts.
- In the /home/ubuntu you can see all the files for Flask as well as the Gunicorn config.
- Gunicorn is tuned for use in a container oriented environment.
- NGINX is tuned for use in a container oriented environment.
