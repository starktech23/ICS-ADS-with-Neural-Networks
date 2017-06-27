#!/usr/bin/python


import os
os.environ['KERAS_BACKEND'] = 'theano'
from config import *
import time
import numpy as np
import logging
from sklearn.cross_validation import train_test_split


# from keras.models import Sequential
# from keras.models import model_from_json
# from keras.layers import Dense, Dropout, Activation, Flatten, LSTM
# from keras.layers import Convolution2D, MaxPooling2D
# from keras.utils import np_utils
# from keras import backend as K
import matplotlib.pyplot as plt
import matplotlib.animation as anim

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylim([0,1])

# json_file = open('model.json', 'r')
# model_json = json_file.read()
# json_file.close()
# model = model_from_json(model_json)
# model.load_weights("model_weights.h5")
x = np.load("train_data.npy")
x=np.reshape(x,(260,1,10))
y = []
# def update(i):
    # t = time.time()
v = []
for t in x:
    v.append(t[0])
print v
               
        # if len(x) == seq:
        #     x = np.array([x])
        #     prediction = model.predict(x, batch_size=1, verbose=0)[0][0]
        #     # if prediction < 0.9:
        #     #     prediction = prediction - 0.15
        #     score = "{0:.2f}".format(prediction)
        #     y.append(score)
        #     ax.clear()
        #     ax.set_title("Neural Network Based Prediction.")
        #     ax.set_xlabel("Evaluation Point")
        #     ax.set_ylabel("Score")
        #     ax.set_ylim([0.5,1.05])
        #     tx = np.array(range(len(y)))*seq
        #     ax.set_xlim([0, 1.5*tx[-1]])
        #     # tx = [tu*seq for tu in tx]
        #     ax.plot(tx, y, "x")
        #     if float(score) < 0.93:
        #         print score, "Compromised"
        #     else:
        #         print score
        #     break

# print "Simulation will start when the time is 0, 25, 50 ,75"
# to = 0
# while 1:
#     toot = int(time.time())%100
#     if to == toot - 1:
#         print toot
#     to = toot
#     # print to
#     if to == 0 or to == 25 or to == 50 or to == 75:
#         break

# a = anim.FuncAnimation(fig, update, frames=int(SIM_TIME/(SIM_STEP*seq)), repeat=False)
# plt.show()