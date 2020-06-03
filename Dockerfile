FROM python:3.7-alpine

MAINTAINER rashmiranjan

ENV PYTHONUNBUFFERED 1

COPY ./requrements.txt/requrements.txt

RUn pip install -r /requrements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user