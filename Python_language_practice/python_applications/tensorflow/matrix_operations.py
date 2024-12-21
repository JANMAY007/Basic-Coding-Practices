import tensorflow as tf
import numpy as np

a=tf.constant([[2,2],[4,5]])
b=tf.constant([[6,1],[3,1]])
print(tf.matmul(a,b))
print(np.array(tf.matmul(a,b)))

c=tf.cast(a,dtype=tf.int32)
print(c)

d=tf.ragged.constant([[1],[],[2,3],[4,5,6]])
print(d)
print(np.array(d))