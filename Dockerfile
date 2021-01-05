FROM debian:10.1-slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y libssl-dev libffi-dev

ENV PYTHONPATH /opt/app/project

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip3 install -r requirements.txt --no-cache-dir

CMD python3 ./project/manage.py runserver 0.0.0.0:8000
