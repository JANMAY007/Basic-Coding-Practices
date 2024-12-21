#!/usr/bin/env python
# coding: utf-8

# # Tensorflow 2.0

# In[5]:


import tensorflow as tf
print(tf.__version__)


# ## Eager Execution

# Previously in tensorflow expresion are not evaluated directly instead computation graph are generated and these graphs are evaluated inside session.
# But now now there is eager execution which means expresions are evaluated immediately and concrete values are returned

# ### Declaring eager variables

# In[8]:


v0 = 42  #python variable
v1 = tf.Variable(42) #rank 0 tensor
v2 = tf.Variable([1,2]) #rank 1 tensor
v3 = tf.Variable([[1,2],[3,4]])  #rank 3 tensor


# In[9]:


v0


# In[10]:


v1


# In[11]:


v2


# In[12]:


v3


# To reassign a variable, use var.assign()

# In[13]:


v1.assign(33)
v1


# ### Declaring TensorFlow constants

# In[15]:


c1 = tf.constant(42)
c1


# you can explicitly specify the datatype

# In[18]:


c2 = tf.constant(62,dtype = tf.float64)
c2


# ### Shaping a tensor

# In[20]:


t4 = tf.Variable([[1,2,3],[4,5,6]])
t4.shape


# or you can reshape a tensor

# In[21]:


t5 = tf.reshape(t4,[1,6])
t5.shape


# In[22]:


t5


# ### Ranking (dimensions) of a tensor

# The rank of a tensor is the number of dimensions it has, that is, the number of indices that are required to specify any particular element of that tensor.

# In[24]:


tf.rank(t4)


# ### Specifying an element of a tensor

# In[25]:


t6 = t4[0,0]
t6


# ### Casting a tensor to a NumPy

# In[27]:


t6.numpy()


# ### Finding the number of elements of a tensor

# In[29]:


tf.size(input = t4).numpy()


# ### Finding the datatype of a tensor

# In[30]:


t6.dtype


# ### Specifying element-wise tensor operations

# In[31]:


t7 = tf.Variable([1,2])
t8  = tf.Variable([2,2])
t7*t8


# In[34]:


(t7*4).numpy()


# ### Transposing and Matrix Multiplication

# In[38]:


c1 = tf.constant([[1,2]])
c2 = tf.constant([[3,4]])
tf.matmul(c1, tf.transpose(a=c2))


# ### Type casting

# In[39]:


c1


# In[41]:


c3 = tf.cast(c1,dtype = tf.int64)
c3


# ### Declaring ragged tensors

# A ragged tensor is a tensor with one or more ragged dimensions. Ragged dimensions are dimensions that have slices that may have different lengths.

# In[43]:


ragged = tf.ragged.constant([[1],[],[1,2],[3,4,5]])
ragged


# ## Tensorflow Operations

# ### Finding the squared difference between two tensors

# In[55]:


v1 = tf.Variable([3,4])
v2 = tf.Variable([2,2])
tf.math.squared_difference(v1,v2 ,name = None)


# ### Finding mean

# In[63]:


tf.reduce_mean(v1)


# mean across rows use axis = 0

# In[64]:


v3 - tf.Variable([[1,2],[3,4]])
tf.reduce_mean(v3, axis = 0)


# mean across rows use axis = 1

# In[68]:


v3 - tf.Variable([[1,2],[3,4]])
tf.reduce_mean(v3, axis = 1)


# ## Generating tensors with random values

# Random values are frequently required when developing neural networks

# ### tf.random.normal()

# In[70]:


tf.random.normal(shape = (3,2), mean = 10, stddev = 2,dtype = tf.float32)


# ### tf.random.uniform()

# In[74]:


tf.random.uniform(shape=(3,2), minval = 0,maxval = 5,dtype = tf.int32)


# if you want the random values generated to be repeatable, then use tf.random.set_seed().

# In[77]:


tf.random.set_seed(111)
tf.random.uniform(shape = (3,2), maxval=10, dtype = tf.int32)


# ### Add two tensors

# In[79]:


v1 = tf.Variable([3,4])
v2 = tf.Variable([2,1])
v1 + v2


# ### Concatinate two tensors

# In[88]:


v1 = tf.Variable([[1,2],
                  [3,4]])
v2 = tf.Variable([[6,7],
                  [8,9]])
v3 = tf.concat(values = [v1,v2],axis = 0)
v3


# In[87]:


v4 = tf.concat(values = [v1,v2],axis = 1)
v4


# ### Finding minimum and maximum element

# In[95]:


v1 = tf.Variable([4,2,3,5])
tf.argmax(input = v1).numpy()


# In[96]:


tf.argmin(input = v1).numpy()


# ## Saving and restoring tensor values using a checkpoint

# In[97]:


variable = tf.Variable([[1,2],[3,4]])
checkpoint = tf.train.Checkpoint(var = variable)
save_path = checkpoint.save('./vars')


# In[98]:


save_path


# In[99]:


variable.assign([[0,0],[0,0]])
variable


# In[100]:


checkpoint.restore(save_path)


# In[101]:


variable


# In[ ]:




