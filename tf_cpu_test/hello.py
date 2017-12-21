import tensorflow as tf
print('hello')
hello = tf.constant('Hello tensorflow CPU')
sess = tf.Session()
print(sess.run(hello))