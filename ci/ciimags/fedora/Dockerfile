FROM fedora

#
# Handle Native package manager update before installing packages
RUN yum -y update && dnf upgrade --refresh

#
# Install required components to simulate best
# test environment.
RUN yum -y install python3
RUN yum -y install python3-pip
RUN yum -y install python3-wheel
RUN yum -y install python-setuptools

RUN yum -y install git-all
RUN yum -y install clang
RUN yum -y install gcc
RUN yum -y install gcc-c++
RUN yum -y install ldc
RUN yum -y install gcc-gfortran
RUN yum -y install gcc-objc
RUN yum -y install gcc-objc++
RUN yum -y install java-devel
RUN yum -y install rustc
RUN yum -y install mono-core
RUN yum -y install mono-devel

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
