import tensorflow as tf
import numpy as np

mat = np.matrix([[1., 2], [3, 4]])
t = tf.nn.softmax(mat, 1)
sess = tf.InteractiveSession()
print(sess.run(t))
t.eval()