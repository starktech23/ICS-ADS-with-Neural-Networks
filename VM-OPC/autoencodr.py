import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers.embeddings import Embedding
from keras.optimizers import Adam
import pandas as pd
import tensorflow as tf
# tf.python.control_flow_ops = tf

df = pd.read_csv('log.csv')
dfX = df[['Close']]
dfY = df[['Y']]
bobX = dfX.as_matrix()
boby = dfY.as_matrix()

model = Sequential()
model.add(Dense(200, input_dim=1))
model.add(Activation('sigmoid'))
model.add(Dense(75))
model.add(Activation('sigmoid'))
model.add(Dense(10))
model.add(Activation('sigmoid'))
model.add(Dense(1))
adam = Adam(lr=0.1)
model.compile(loss='mse', optimizer= adam)
print(model.summary())

model.fit(bobX, boby, nb_epoch=2500, batch_size=500, verbose=0)

model.predict(np.array([[210.99]]))