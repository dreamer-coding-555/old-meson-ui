FROM debian:buster

#
# Handle Native package manager update before installing packages
RUN apt-get update --fix-missing && apt-get upgrade -y

#
# Install required components to simulate best
# test environment.
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-wheel
RUN apt-get -y install python-setuptools
RUN apt-get -y install python3-pyqt5

RUN apt-get -y install git-all
RUN apt-get -y install libxml2-dev
RUN apt-get -y install libxslt1-dev
RUN apt-get -y install libyaml-dev
RUN apt-get -y install libjson-glib-dev
RUN apt-get -y install libc6-dev
RUN apt-get -y install clang
RUN apt-get -y install gcc
RUN apt-get -y install g++
RUN apt-get -y install ldc
RUN apt-get -y install gfortran
RUN apt-get -y install gobjc
RUN apt-get -y install gobjc++
RUN apt-get -y install default-jre
RUN apt-get -y install rustc
RUN apt-get -y install mono-complete

#
# Handle pip update before installing packages
RUN pip3 install --upgrade pip

#
# Install packager teamed necessary for Meson-UI 
RUN pip3 install meson==0.53.2
RUN pip3 install ninja==1.9.0
RUN pip3 install PyQt5==5.14.1

#
# packagers needed for CI and unit testing.
RUN pip3 install codecov==2.0.15
RUN pip3 install pytest==5.3.2
RUN pip3 install pytest-qt==3.3.0
RUN pip3 install pytest-cov==2.8.1
RUN pip3 install pytest-mock==1.13.0
