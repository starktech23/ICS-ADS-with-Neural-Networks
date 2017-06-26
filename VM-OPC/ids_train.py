#!/usr/bin/python
#Required Libraries
import os
os.environ['KERAS_BACKEND'] = 'theano'
from config import *
from pymodbus.client.sync import ModbusTcpClient
import time
import numpy as np
import pandas as pd
import logging
# from sklearn.cross_validation import train_test_split
# from keras.models import Sequential
# from keras.models import model_from_json
# from keras.layers import Dense, Dropout, Activation,Flatten,LSTM,GRU
# from keras.layers import Convolution2D, MaxPooling2D
# from keras.utils import np_utils
# from keras import backend as K
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#Get Dataset
df=pd.read_csv('log.csv',engine='python')
a=df.dropna(axis=0,how='any')
print a
Data=df.values

print Data
Data=Data.astype('float32')
#normalize the dataset
# scaler=MinMaxScaler(feature_range=(0,1))
# Data=scaler.fit_transform(Data)

def create_dataset(Data,look_back=1):
	Xdata,Ydata=[],[]
	for i in range(len(Data)-look_back-1):
		a=Data[i:(i+look_back),0]
		print a
		Xdata.append(a)
		b=Data[i+look_back,0]
		print b
		Ydata.append(b)
	return np.array(Xdata),np.array(Ydata)
np.random.seed(7)
create_dataset(Data,look_back)
		
# print Data
# Data = Data[:Data.shape[0]/3]
# print Data
# X = []
# for i in range(Data.shape[0]-seq-padding):
#     t = padding
#     tmp = []
#     while t < seq + padding:
#         tmp.append(Data[t + i])
#         t += 1
#     X.append(tmp)

# X = np.array(Data)
# print X
# Y = [1 for i in range(X.shape[0])]

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20,random_state=42)

# print X.shape



# import os
# os.environ['KERAS_BACKEND'] = 'theano'
# from pandas import concat #funcction concatinates two columns 
# from pandas import DataFrame#converts into dataframe
# from keras.models import Sequential#a type of data strucure that gives a sequence of blocks
# from keras.layers import Dense,Dropout,Flatten,Activation #no of layers
# from keras.layers import LSTM,GRU#model to be used
# from config import *
# from itertools import count
# from sklearn.cross_validation import train_test_split
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# data = np.load("train_data.npy")
# X=data
# y = [1 for i in range(X.shape[0])]
# n_batch=26
# n_epoch = 10
# n_neurons= 10
# n_classes=1

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,)
# X_train = X_train.astype('float32')
# X_test = X_test.astype('float32')
# # print X_train
# print('X_train shape:', X_train.shape)
# print(X_train.shape[0], 'train samples')
# print(X_test.shape[0], 'test samples')
# seq=20
# print y_train
# #compile model
# model=Sequential()
# # model.add(LSTM(n_neurons,batch_input_shape=(X_train.shape[0],X_train.shape[1]),stateful=True))

# model.add(LSTM(10, batch_input_shape = (1,X_train.shape[1],X_train.shape[0]),stateful=True))
# model.add(Dense(1,activation='sigmoid'))
# model.compile(loss='mean_squared_error',optimizer='adam')	
# #fit network
# print(model.summary())
# model.fit(X_train,y_train,epochs=n_epoch,batch_size=n_batch,verbose=1,shuffle=False)
# #forecast

# score = model.evaluate(X_test, y_test, verbose=0)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])















































# # # create sequence
# # length = 10
# # sequence = [i/float(length) for i in range(length)]
# # # create X/y pairs
# # df = DataFrame(sequence)
# # df = concat([df, df.shift(1)], axis=1)#df.shift(1) makes a new column of elements with 1 increment and df.concat concatenates the two columns  
# # df.dropna(inplace=True)#drop columns with na element any then any nan or all if all elements are nan
# # #print(df)
# # #convert to lstm friendly format
# # values=df.values#stores values of datafrmae in values as a list of list
# # print values
# # X,y=values[:,0],values[:,1]#converts a list of list into single list
# # print X,y
# # X=X.reshape(len(X),1,1)#features (len(X,1) and and time step is 1
# # print X
# # print X.shape,y.shape

# # #configure network
# # n_batch = 1

# # n_epoch = 1000
# # n_neurons= 10
# # #design network
# # model=Sequential()
# # model.add(LSTM(n_neurons,batch_input_shape=(n_batch,X.shape[1],X.shape[2]),stateful=True))
# # model.add(Dense(1))
# # model.compile(loss='mean_squared_error',optimizer='adam')
# # # re-define the batch size
# # n_batch = 1
# # # re-define model
# # new_model = Sequential()
# # new_model.add(LSTM(n_neurons, batch_input_shape=(n_batch, X.shape[1], X.shape[2]), stateful=True))
# # new_model.add(Dense(1))
# # # copy weights
# # old_weights = model.get_weights()
# # new_model.set_weights(old_weights)
# # # batch forecast
# # yhat = model.predict(X, batch_size=n_batch)
# # for i in range(len(y)):
# # 	print('>Expected=%.1f, Predicted=%.1f' % (y[i], yhat[i]))


# # #fit network
# # for i in range(n_epoch):
# # 	model.fit(X,y,epochs=1,batch_size=n_batch,verbose=1,shuffle=False)
# # #forecast
# # for i in range(len(X)):
# # 	testX, testy = X[i], y[i]
# # 	testX = testX.reshape(1, 1, 1)
# # 	yhat = model.predict(testX, batch_size=1)
# # 	print('>Expected=%.1f, Predicted=%.1f' % (testy, yhat))


