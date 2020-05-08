FROM python:3.6-buster

RUN apt-get -y update && apt-get install -y apt-utils ca-certificates

RUN update-ca-certificates

RUN pip install psycopg2