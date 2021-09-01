# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster AS opencv
RUN apt-get update
RUN apt-get -y install cmake g++ wget unzip imagemagick
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
RUN unzip opencv.zip
RUN mkdir -p build && cd build
WORKDIR ./build
RUN cmake  ../opencv-master
RUN cmake --build .
RUN make install


FROM python:3.9-slim-buster AS app

RUN export APP_ENV=DOCKER-DEV
RUN apt-get update

COPY --from=opencv /usr/local/bin /usr/local/bin
COPY --from=opencv /usr/local/lib /usr/local/lib
COPY --from=opencv /usr/local/cmake/opencv4 /usr/local/cmake/opencv4
COPY --from=opencv /usr/local/include/opencv4 /usr/local/include/opencv4
COPY --from=opencv /usr/local/share/opencv4 /usr/local/share/opencv4

RUN apt-get -y install tesseract-ocr imagemagick

# Install the application
RUN mkdir -p /server && cd /server

WORKDIR ./server
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
COPY . .


RUN export PYTHONPATH=./src
RUN python3 -m site

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

CMD [ "python3", "-m" , "site"]