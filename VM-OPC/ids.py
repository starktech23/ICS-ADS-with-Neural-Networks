#!/usr/bin/python
#MTU Server

import os
os.environ['KERAS_BACKEND'] = 'theano'
# os.environ['THEANO_FLAGS'] = 'floatX=float32,device=gpu,lib.cnmem=0.8,dnn.conv.algo_bwd_filter=deterministic,dnn.conv.algo_bwd_data=deterministic,blas.ldflags=-LC:/toolkits/openblas-0.2.14-int32/bin -lopenblas'
from config import *
from pymodbus.client.sync import ModbusTcpClient
import time
import numpy as np
import itertools
import logging
from sklearn.cross_validation import train_test_split


from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

import matplotlib.pyplot as plt
import matplotlib.animation as anim

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)


json_file = open('final_model.json', 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("final_model_weights.h5")

test=np.load("mal1_test_data.npy")
test_data=np.reshape(test,(260,1,10))



pred= model.predict(test_data,batch_size=1,verbose=1)
prediction = pred.tolist()
predict_list_temp = list(sum(prediction, []))
predict_list = list(sum(predict_list_temp, []))


predict=np.reshape(pred,(260,10))
plt.plot(predict)
plt.ylim(0.93,1.0)
plt.xlim(20,260)
plt.title("Neural Network Based Prediction.")
plt.xlabel("Evaluation Point")
plt.ylabel("Score")
plt.show()