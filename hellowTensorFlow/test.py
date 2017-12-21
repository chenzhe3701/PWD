import tensorflow as tf

sess = tf.Session()
print(sess.run(tf.squared_difference(5, 2)))