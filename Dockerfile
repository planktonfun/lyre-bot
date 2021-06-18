FROM python:3.9.2
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN apt update -y
RUN apt install -y ffmpeg libavcodec-extra

COPY . /app