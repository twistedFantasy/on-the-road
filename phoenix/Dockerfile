FROM python:3.10.4
LABEL maintainer="Denis Sventitsky <denis.sventitsky@gmail.com> / Twisted Fantasy <twisteeed.fantasy@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/phoenix/

RUN mkdir -p /usr/src/phoenix/
WORKDIR /usr/src/phoenix/

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .
