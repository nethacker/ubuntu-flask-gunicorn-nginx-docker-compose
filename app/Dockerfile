# VERSION 1.0
# AUTHOR: Phil Chen
# DOCKER HUB: https://hub.docker.com/u/nethacker
# DESCRIPTION: A scalable Flask application using Gunicorn on Ubuntu 18.04
# SOURCE: https://github.com/nethacker/ubuntu-flask-gunicorn-nginx-docker-compose
FROM nethacker/ubuntu-18-04-python-3:python-3.7.3
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*
RUN pip install gunicorn flask && useradd -m ubuntu
ENV HOME=/home/ubuntu
USER ubuntu
COPY src/app01.py src/wsgi.py src/gunicorn_config.py /home/ubuntu/
WORKDIR /home/ubuntu/
EXPOSE 8080
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:hello"]
