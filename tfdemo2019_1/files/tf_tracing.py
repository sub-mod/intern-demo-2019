import os, sys, time, tensorflow as tf, numpy as np

def run_resnet50(batch_size, ompnumthreads, interop, intraop): 
  # Threading Parameters
  os.environ['OMP_NUM_THREADS'] = str(ompnumthreads) 
  os.environ['KMP_BLOCKTIME'] = '1'
  os.environ['KMP_AFFINITY' ] = 'granularity=fine,compact,1,0' 
  os.environ['KMP_SETTINGS' ] = '0'

  # Enable Tracing
  run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
  run_metadata = tf.RunMetadata()
  model = tf.keras.applications.ResNet50(weights=None)
  model.compile(tf.keras.optimizers.SGD(), loss='categorical_crossentropy', options=run_options, run_metadata=run_metadata) 
  dummy_x = np.zeros((batch_size, 224, 224, 3), dtype='float32')
  dummy_y = np.zeros((batch_size, 1000), dtype='float32')

  # Threading Config
  config = tf.ConfigProto(intra_op_parallelism_threads=intraop, inter_op_parallelism_threads=interop, allow_soft_placement=True)

  # model training
  with tf.Session(config=config): 
    tm = time.time()
    model.fit(dummy_x, dummy_y) 
    tm = time.time() - tm

  # Save tensorflow timeline
  from tensorflow.python.client import timeline
  trace = timeline.Timeline(step_stats=run_metadata.step_stats) 
  with open('timeline.json', 'w') as f:
    f.write(trace.generate_chrome_trace_format()) 
  return float(batch_size)/tm
if __name__ == '__main__':
  batch_size, ompnumthreads = int(sys.argv[1]), int(sys.argv[2]) 
  interop, intraop = int(sys.argv[3]), int(sys.argv[4]) 
  run_resnet50(batch_size, ompnumthreads, interop, intraop)