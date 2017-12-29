from __future__ import print_function

import tensorflow as tf

hello = tf.constant('Hello TensorFlow!')
s = tf.Session()
print(s.run(hello))
