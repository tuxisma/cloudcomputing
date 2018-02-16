FROM ubuntu:latest
MAINTAINER Ismael Garcia <tuxisma@gmail.com>
RUN apt-get update && \
    apt-get install -y wget  

RUN wget --quiet https://github.com/gohugoio/hugo/releases/download/v0.31.1/hugo_0.31.1_Linux-64bit.tar.gz && \
    tar -xf hugo_0.31.1_Linux-64bit.tar.gz && \
    chmod +x hugo && \
    mv hugo /usr/local/bin/hugo && \
    rm -rf hugo_0.31.1_Linux-64bit.tar.gz

RUN mkdir /usr/share/blog
WORKDIR /usr/share/blog

EXPOSE 1313

ADD . /usr/share/blog

ENV HUGO_BASE_URL http://localhost:1313
CMD hugo server -b ${HUGO_BASE_URL} --bind=0.0.0.0

