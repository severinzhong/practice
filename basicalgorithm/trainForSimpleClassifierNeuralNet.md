

```python
import numpy as np 
import pandas as pd 
import sys, os 
import tensorflow as tf

from time import time
```


```python
dirpath = "dataset/trainSet.txt"
data = np.loadtxt(dirpath)
data.shape
```




    (6767070, 4)




```python
dirpath = "dataset/testSet.txt"
testdata = np.loadtxt(dirpath)
testdata.shape
```




    (3995931, 4)




```python
X , Y = data[: , :2] / 120. + 0.7 , data[: , 2:]
X.shape , Y.shape
```




    ((6767070, 2), (6767070, 2))




```python
X_ , Y_ = testdata[: , :2] / 120. + 0.7 , testdata[: , 2:]
X_.shape , Y_.shape
```




    ((3995931, 2), (3995931, 2))




```python
##build the net
w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
b1 = tf.Variable(tf.random_normal([1],stddev=1,seed=1))

w2 = tf.Variable(tf.random_normal([3,2],stddev=1,seed=1))
b2 = tf.Variable(tf.random_normal([1],stddev=1,seed=1))

x = tf.placeholder(tf.float32,shape=(None,2),name="x-input")
y_ = tf.placeholder(tf.float32,shape=(None,2),name="y-input")

a = tf.nn.sigmoid(tf.matmul(x,w1) + b1)
#y = tf.nn.sigmoid(tf.matmul(a,w2) + b2)
y = tf.nn.softmax(tf.matmul(a,w2) + b2)

# cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y,1e-10,1.0))+(1-y_) * tf.log(tf.clip_by_value(1-y,1e-10,1.0)))
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), axis=1))

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

dataset_size = data.shape[0]
batch_size = 16  
```


```python

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    steps = 50001
    for i in range(steps):
            start = (i * batch_size) % dataset_size
            end = min(start + batch_size,dataset_size)
            
            sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
            
            if i % (steps / 10) == 0 :
                
                total_cross_entropy = sess.run(cross_entropy,feed_dict={x:X,y_:Y})
                total_accuracy = sess.run(accuracy,feed_dict={x:X,y_:Y})
                print("After %d training step(s),cross entropy on all data is %g , accuracy %g"%(i,total_cross_entropy,total_accuracy))
    ## test 
    print("test data : cross entropy %g ,Accuracy %g"% (
        sess.run(cross_entropy,feed_dict={x:X_,y_:Y_}) ,
        sess.run(accuracy,feed_dict={x:X_,y_:Y_})
    ) )
```

    After 0 training step(s),cross entropy on all data is 0.762281 , accuracy 0.255687
    After 5000 training step(s),cross entropy on all data is 0.516191 , accuracy 0.710269
    After 10000 training step(s),cross entropy on all data is 0.45551 , accuracy 0.769955
    After 15000 training step(s),cross entropy on all data is 0.43593 , accuracy 0.779242
    After 20000 training step(s),cross entropy on all data is 0.420297 , accuracy 0.800425
    After 25000 training step(s),cross entropy on all data is 0.376902 , accuracy 0.82005
    After 30000 training step(s),cross entropy on all data is 0.399772 , accuracy 0.808655
    After 35000 training step(s),cross entropy on all data is 0.385229 , accuracy 0.819975
    After 40000 training step(s),cross entropy on all data is 0.385766 , accuracy 0.820069
    After 45000 training step(s),cross entropy on all data is 0.404234 , accuracy 0.797816
    After 50000 training step(s),cross entropy on all data is 0.321475 , accuracy 0.85129
    test data : cross entropy 0.187379 ,Accuracy 0.920542



```python

```
