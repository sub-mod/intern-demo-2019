FROM registry.fedoraproject.org/f28/python3
MAINTAINER Subin Modeel <smodeel@redhat.com>

USER root
COPY ./files /demo_files
COPY ./thoth /thoth

RUN yum install -y yum-utils scl-utils gdb wget vim tree dnf-plugins-core \
    && dnf debuginfo-install -y python bzip2-libs-1.0.6-26.fc28.x86_64 libffi-3.1-16.fc28.x86_64 libgcc-8.2.1-4.fc28.x86_64 libstdc++-8.2.1-4.fc28.x86_64 ncurses-libs-6.1-5.20180224.fc28.x86_64 openssl-libs-1.1.0h-3.fc28.x86_64 python3-libs-3.6.5-1.fc28.x86_64 readline-7.0-11.fc28.x86_64 xz-libs-5.2.4-2.fc28.x86_64 zlib-1.2.11-8.fc28.x86_64 \
    && dnf debuginfo-install -y glibc-2.27-32.fc28.x86_64 \
	&& pip install pipenv \
	&& pip install pyarrow==0.13.0 \
	&& pip install tensorflow==1.13.1


CMD ["/bin/bash"]
