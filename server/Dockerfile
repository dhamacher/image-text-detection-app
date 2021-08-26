# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

# Install Tesseract-OCR
#If you are using a different Linux distribution, you’ll need to copy the last github repository version and copy the
#.traineddata file into ‘tessdata’ (/usr/share/tesseract-ocr/tessdata or /usr/share/tessdata).
RUN apt-get update
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install imagemagick

WORKDIR /server

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]