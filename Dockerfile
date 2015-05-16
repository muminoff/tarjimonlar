FROM python:2.7
MAINTAINER: muminoff
WORKDIR /tarjimonlar
ADD . /tarjimonlar
RUN apt-get update -y
RUN pip install -r requirements.txt
