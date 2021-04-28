# The format (or template) of docker file is always as below:
#  FROM operating system of our machine
FROM ubuntu:18.04
#
WORKDIR /app
COPY . .

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN echo "$PWD"
RUN python -m pip install pip==21.0.1
RUN pip install -r requirment.txt

CMD  python SentimentTwitter.py
