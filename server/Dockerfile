# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster AS app

RUN apt-get update && \
    apt-get -y install tesseract-ocr imagemagick python3-opencv

WORKDIR /server

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt && \
    mkdir -p uploaded_images && \
    mkdir -p output && \
    mkdir -p logs && \
    export PYTHONPATH=/server/src && \
    export APP_ENV=DOCKER-DEV
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]