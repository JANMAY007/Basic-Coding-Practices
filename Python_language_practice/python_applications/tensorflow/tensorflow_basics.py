import tensorflow as tf
import numpy as np

a=tf.constant(42)
print(a)

b=tf.constant(24,dtype=float)
print(b)

c=tf.Variable([[1,2,3],[4,5,6]])
print(c)
print(tf.rank(c))
d=tf.reshape(c,[1,6])
print(d)
print(tf.rank(d))

e=c[0,0]
print(e)
f=np.array(e)
print(f)

print(tf.size(input=c))
print(np.array(tf.size(input=c)))