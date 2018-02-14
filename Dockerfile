FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN apt-get update && apt-get upgrade -y && apt-get install libmysqlclient-dev -y
RUN pip3 install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src