from pandas import concat #funcction concatinates two columns 
from pandas import DataFrame#converts into dataframe
# from keras.models import Sequential#a type of data strucure that gives a sequence of blocks
# from keras.layers import Dense#no of layers
# from keras.layers import LSTM#model to be used
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("out.csv","r",usecols=[0], engine='python', skipfooter=0)
values=df.values
#print values
data_array=np.array(values)
print data_array

plt.plot(data_array)
plt.show()




















































# # create sequence
# length = 10
# sequence = [i/float(length) for i in range(length)]
# # create X/y pairs
# df = DataFrame(sequence)
# df = concat([df, df.shift(1)], axis=1)#df.shift(1) makes a new column of elements with 1 increment and df.concat concatenates the two columns  
# df.dropna(inplace=True)#drop columns with na element any then any nan or all if all elements are nan
# #print(df)
# #convert to lstm friendly format
# values=df.values#stores values of datafrmae in values as a list of list
# print values
# X,y=values[:,0],values[:,1]#converts a list of list into single list
# print X,y
# X=X.reshape(len(X),1,1)#features (len(X,1) and and time step is 1
# print X
# print X.shape,y.shape

# #configure network
# n_batch = 1

# n_epoch = 1000
# n_neurons= 10
# #design network
# model=Sequential()
# model.add(LSTM(n_neurons,batch_input_shape=(n_batch,X.shape[1],X.shape[2]),stateful=True))
# model.add(Dense(1))
# model.compile(loss='mean_squared_error',optimizer='adam')
# # re-define the batch size
# n_batch = 1
# # re-define model
# new_model = Sequential()
# new_model.add(LSTM(n_neurons, batch_input_shape=(n_batch, X.shape[1], X.shape[2]), stateful=True))
# new_model.add(Dense(1))
# # copy weights
# old_weights = model.get_weights()
# new_model.set_weights(old_weights)
# # batch forecast
# yhat = model.predict(X, batch_size=n_batch)
# for i in range(len(y)):
# 	print('>Expected=%.1f, Predicted=%.1f' % (y[i], yhat[i]))


# #fit network
# for i in range(n_epoch):
# 	model.fit(X,y,epochs=1,batch_size=n_batch,verbose=1,shuffle=False)
# #forecast
# for i in range(len(X)):
# 	testX, testy = X[i], y[i]
# 	testX = testX.reshape(1, 1, 1)
# 	yhat = model.predict(testX, batch_size=1)
# 	print('>Expected=%.1f, Predicted=%.1f' % (testy, yhat))


