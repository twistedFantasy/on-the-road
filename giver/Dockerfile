FROM python:3.10.4
LABEL maintainer="Denis Sventitsky <denis.sventitsky@gmail.com> / Twisted Fantasy <twisteeed.fantasy@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/giver/

RUN mkdir -p /usr/src/giver/
WORKDIR /usr/src/giver/

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .
