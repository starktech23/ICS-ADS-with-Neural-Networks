# #!/usr/bin/python

from random import randint
from numpy import array
from numpy import argmax
import numpy as np
from pandas import DataFrame
from pandas import concat
import pandas as pd

x = np.load("train_data.npy")
x = x.astype('int32')
x_list=x.tolist()#a list of list of all the readings
sequence=[]
for sublist in x_list:
    for item in sublist:
        sequence.append(item) #complete list of all the readings
# one hot encode sequence

def one_hot_encode(sequence, n_unique=1000):
    encoding = list()
    for value in sequence:
        vector = [0 for _ in range(n_unique)]
        vector[value] = 1
        encoding.append(vector)
    # print encoding
    return array(encoding)

# decode a one hot encoded string
def one_hot_decode(encoded_seq):
    return [argmax(vector) for vector in encoded_seq]

# convert encoded sequence to supervised learning
def to_supervised(sequence, n_in, n_out):
    # create lag copies of the sequence
    # df = DataFrame(sequence)
    # df = concat([df.shift(n_in-i-1) for i in range(n_in)], axis=1)
    # drop rows with missing values
    # df.dropna(inplace=True)
    # specify columns for input and output pairs
    # values = df.values
    width = x.shape[1]
    print width 
    X = x.reshape(len(x), n_in, width)
    y = x[:, 0:(n_out*width)].reshape(len(x), n_out, width)
    return X, y

# generate random sequence


# one hot encode
encoded = one_hot_encode(sequence)
# convert to X,y pairs
X,y = to_supervised(encoded, 5, 3)
# decode all pairs
for i in range(len(X)):
    print(one_hot_decode(X[i]), '=>', one_hot_decode(y[i]))

# import os
# os.environ['KERAS_BACKEND'] = 'theano'
# from config import *
# import time
# import numpy as np
# import logging
# from sklearn.cross_validation import train_test_split
# from mpl_toolkits.mplot3d import Axes3D

# from keras.models import Sequential
# from keras.models import model_from_json
# from keras.layers import Dense, Dropout, Activation, Flatten, LSTM
# from keras.layers import Convolution2D, MaxPooling2D
# from keras.utils import np_utils
# from keras import backend as K
# import matplotlib.pyplot as plt
# import matplotlib.animation as anim

# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.INFO)


# # fig = plt.figure()
# # ax = fig.add_subplot(1,1,1)
# # ax.set_ylim([0,1])

# json_file = open('new1_model.json', 'r')
# model_json = json_file.read()
# json_file.close()
# model = model_from_json(model_json)
# model.load_weights("new2_model_weights.h5")
# x = np.load("train_data.npy")
# x=np.reshape(x,(260,1,10))
# y=np.ones((260,10))
# y=np.reshape(y,(260,1,10))
# # def update(i):
#     # t = time.time()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x)
# ax.show()
# v = []

# scores=[]

# eval= model.predict(x,batch_size=1,verbose=0)[0][0]
# print eval.shape
# print eval
# plt.plot(eval)
# e=model.predict(x,batch_size=1,verbose=0)[0][0]
# print e
# plt.plot(e)
# plt.show()
               
#         # if len(x) == seq:
#         #     x = np.array([x])
#         #     prediction = model.predict(x, batch_size=1, verbose=0)[0][0]
#         #     # if prediction < 0.9:
#         #     #     prediction = prediction - 0.15
#         #     score = "{0:.2f}".format(prediction)
#         #     y.append(score)
#         #     ax.clear()
#         #     ax.set_title("Neural Network Based Prediction.")
#         #     ax.set_xlabel("Evaluation Point")
#         #     ax.set_ylabel("Score")
#         #     ax.set_ylim([0.5,1.05])
#         #     tx = np.array(range(len(y)))*seq
#         #     ax.set_xlim([0, 1.5*tx[-1]])
#         #     # tx = [tu*seq for tu in tx]
#         #     ax.plot(tx, y, "x")
#         #     if float(score) < 0.93:
#         #         print score, "Compromised"
#         #     else:
#         #         print score
#         #     break



# # a = anim.FuncAnimation(fig, update, frames=int(SIM_TIME/(SIM_STEP*seq)), repeat=False)
# # plt.show()
