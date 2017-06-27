#!/usr/bin/python
#MTU Server

import os
os.environ['KERAS_BACKEND'] = 'theano'
# os.environ['THEANO_FLAGS'] = 'floatX=float32,device=gpu,lib.cnmem=0.8,dnn.conv.algo_bwd_filter=deterministic,dnn.conv.algo_bwd_data=deterministic,blas.ldflags=-LC:/toolkits/openblas-0.2.14-int32/bin -lopenblas'
from config import *
from pymodbus.client.sync import ModbusTcpClient
import time
import numpy as np
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

opc1_client = ModbusTcpClient(OPC1_IP, OPC1_PORT)
opc1_client.connect()
opc2_client = ModbusTcpClient(OPC2_IP, OPC2_PORT)
opc2_client.connect()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylim([0,1])

json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("model_weights.h5")


y = []
def update(i):
    t = time.time()
    x = []
    while True:
        while time.time()-t < SIM_STEP:
            continue
        t = time.time()
        l1 = float(opc1_client.read_holding_registers(L1, 1).registers[0])
        l2 = float(opc2_client.read_holding_registers(L2, 1).registers[0])
        t1 = float(opc1_client.read_holding_registers(T1, 1).registers[0])
        t2 = float(opc2_client.read_holding_registers(T2, 1).registers[0])
        v1 = opc2_client.read_holding_registers(V1, 1).registers[0]
        v2 = opc1_client.read_holding_registers(V2, 1).registers[0]
        p  = opc2_client.read_holding_registers( P, 1).registers[0]
        f1 = opc2_client.read_holding_registers(F1, 1).registers[0]
        f2 = opc1_client.read_holding_registers(F2, 1).registers[0]
        f3 = opc2_client.read_holding_registers(F3, 1).registers[0]
        h  = opc1_client.read_holding_registers( H, 1).registers[0]

        v = [l1, l2, t1, t2, v1, v2, p, f1, f2, f3, h]
        x.append(v)
        if len(x) == seq:
            x = np.array([x])
            prediction = model.predict(x, batch_size=1, verbose=0)[0][0]
            # if prediction < 0.9:
            #     prediction = prediction - 0.15
            score = "{0:.2f}".format(prediction)
            y.append(score)
            ax.clear()
            ax.set_title("Neural Network Based Prediction.")
            ax.set_xlabel("Evaluation Point")
            ax.set_ylabel("Score")
            ax.set_ylim([0.5,1.05])
            tx = np.array(range(len(y)))*seq
            ax.set_xlim([0, 1.5*tx[-1]])
            # tx = [tu*seq for tu in tx]
            ax.plot(tx, y, "x")
            if float(score) < 0.93:
                print score, "Compromised"
            else:
                print score
            break

print "Simulation will start when the time is 0, 25, 50 ,75"
to = 0
while 1:
    toot = int(time.time())%100
    if to == toot - 1:
        print toot
    to = toot
    # print to
    if to == 0 or to == 25 or to == 50 or to == 75:
        break

a = anim.FuncAnimation(fig, update, frames=int(SIM_TIME/(SIM_STEP*seq)), repeat=False)
plt.show()