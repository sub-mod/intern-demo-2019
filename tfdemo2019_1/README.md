


[Tensorflow Build](https://github.com/thoth-station/tensorflow-build-s2i)  

[AICOE Pypi](https://tensorflow.pypi.thoth-station.ninja)  


```docker build -t submod/tfdemo2019_1 -f Dockerfile .```  
  
```docker run -it -u 0 -v $(pwd):/input:Z --privileged submod/tfdemo2019_1 /bin/bash```  
  
```python tf_tracing.py 100 2 2 2```  
  
```/demo_files/test_app.sh ```  
  
  