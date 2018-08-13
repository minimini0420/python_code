import tensorflow as tf

a = tf.placeholder(tf.int32, [None])
b = tf.constant(10)

x10_op = a/b

sess = tf.Session()

r1 = sess.run(x10_op, feed_dict={a:[2,4,6,8,10]})
print(r1)
r2 = sess.run(x10_op, feed_dict={a:[10,20]})
print(r2)