

```docker build -t submod/tfdemo2019_2 -f Dockerfile .```

```docker run -it -u 0 -v $(pwd):/input:Z --privileged submod/tfdemo2019_2 /bin/bash```


```
python
import tensorflow


objdump -p  /opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/tensorflow/libtensorflow_framework.so |grep NEEDED  
objdump -T /lib64/libc.so.6   
objdump -T /lib64/libc.so.6  |grep GLIBC_2.1  

```
