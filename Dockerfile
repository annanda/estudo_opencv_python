FROM ubuntu:14.04
MAINTAINER Annanda Sousa <annanda.sousa@gmail.com>

RUN apt-get update \
	&& apt-get install -y python python-dev python-pip python-opencv python-matplotlib
