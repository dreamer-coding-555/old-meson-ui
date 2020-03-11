FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV LANG='C.UTF-8'

#
# Handle Native package manager update before installing packages
RUN apt-get update && apt-get upgrade -y

#
# Install required components to simulate best
# test environment.
RUN sed -i '/^#\sdeb-src /s/^#//' "/etc/apt/sources.list"
RUN apt-get -y install eatmydata
RUN eatmydata apt-get -y install python3
RUN eatmydata apt-get -y install python3-pip
RUN eatmydata apt-get -y install python3-wheel
RUN eatmydata apt-get -y install python-setuptools
RUN eatmydata apt-get -y install python3-pyqt5

RUN eatmydata apt-get -y install git-all
RUN eatmydata apt-get -y install libxml2-dev
RUN eatmydata apt-get -y install libxslt1-dev
RUN eatmydata apt-get -y install libyaml-dev
RUN eatmydata apt-get -y install libjson-glib-dev
RUN eatmydata apt-get -y install libc6-dev
RUN eatmydata apt-get -y install clang
RUN eatmydata apt-get -y install gcc
RUN eatmydata apt-get -y install g++
RUN eatmydata apt-get -y install ldc
RUN eatmydata apt-get -y install gfortran
RUN eatmydata apt-get -y install gobjc
RUN eatmydata apt-get -y install gobjc++
RUN eatmydata apt-get -y install default-jre

#
# Handle pip update before installing packages
RUN eatmydata pip3 install --upgrade pip

#
# Install packager teamed necessary for Meson-UI 
RUN eatmydata pip3 install meson==0.53.2
RUN eatmydata pip3 install cmake==3.16.3
RUN eatmydata pip3 install ninja==1.9.0
RUN eatmydata pip3 install PyQt5==5.14.1
RUN eatmydata pip3 install hotdoc==0.10.0

#
# packagers needed for CI and unit testing.
RUN eatmydata pip3 install codecov==2.0.15
RUN eatmydata pip3 install pytest==5.3.2
RUN eatmydata pip3 install pytest-qt==3.3.0
RUN eatmydata pip3 install pytest-cov==2.8.1
RUN eatmydata pip3 install pytest-mock==1.13.0
