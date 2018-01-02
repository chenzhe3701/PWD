# some expressions that might be useful

import tensorflow as tf

# method-1: simple linear regression model (from for beginners, section-1)
# (1) first, define the function
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x+b
y = tf.placeholder(tf.float32)
loss = tf.reduce_sum(tf.square(linear_model-y))
# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# (2) Then, run the training steps to minimize the loss function
train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)  # initialize/reset values to wrong
for i in range(1000):
    sess.run(train, {x: x_train, y: y_train})

# method-2