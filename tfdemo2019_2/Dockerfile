FROM quay.io/aicoe/manylinux2010_x86_64
MAINTAINER Subin Modeel <smodeel@redhat.com>


ADD ./etc/profile.d/enablepython36.sh /etc/profile.d/
COPY ./files /demo_files

RUN yum install -y yum-utils scl-utils gdb wget scl-utils rh-python36 vim tree
SHELL [ "/usr/bin/scl", "enable", "rh-python36" ]
RUN python -V \
    && python /demo_files/get-pip.py \
    && pip install /demo_files/pyarrow*.whl \
    && pip install /demo_files/tensorflow*.whl


CMD ["/bin/bash"]
