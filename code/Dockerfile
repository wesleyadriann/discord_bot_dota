FROM python:3.7-alpine3.10

RUN apk update && \
  apk add bash py-pip && \
  apk add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev make && \
  pip --no-cache-dir install -U pip && \
  apk del --purge build


RUN apk add --update \
    supervisor \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    gcc \
    libxml2-dev \
    zlib-dev \
    libxslt-dev \
    libffi-dev \
    libressl-dev

#  libxslt1-dev \ libssl-dev \     zlib1g-dev \

COPY ./requirements.txt /requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

WORKDIR /app

COPY ./app .

ENV DISCORD_BOT_KEY "key"

ENTRYPOINT python __init__.py
