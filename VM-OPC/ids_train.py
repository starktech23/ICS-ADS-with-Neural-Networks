#Required Libraries
import os
os.environ['KERAS_BACKEND'] = 'theano'
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense, Embedding,Dropout, Activation,Flatten,LSTM,GRU
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from sklearn.preprocessing import MinMaxScaler
from keras.utils.vis_utils import plot_model,model_to_dot
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import Normalizer
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
#Getting Dataset
X = np.load("train_data.npy")
Y=np.ones((260,10))

#Splitting Dataset
train_size=int(len(X)*0.80)
test_size=len(X)-train_size
X_train,X_test=X[0:train_size,:],X[train_size:len(X),:]
Y_train,Y_test=Y[0:train_size,:],Y[train_size:len(Y),:]
X_train=np.array(X_train)
X_test=np.array(X_test)

X_train = X_train.astype('int32')
X_test = X_test.astype('int32')
length=10
#Reshape array
X_train=np.reshape(X_train,(208,1,length))
Y_train=np.reshape(Y_train,(208,1,length))
X_test=np.reshape(X_test,(52,1,length))
Y_test=np.reshape(Y_test,(52,1,length))
#Configure Net
model=Sequential()
model.add(LSTM(10,batch_input_shape=(1,1,length),return_sequences=True,activation='sigmoid'))
print model.input_shape
print model.output_shape
model.add(Dense(10,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(X_train,Y_train,validation_data=(X_test, Y_test),epochs=10,batch_size=1,verbose=1,shuffle=False)
print(model.summary())
   
print(history.history.keys())  
   
plt.figure(1)  
   
 # summarize history for accuracy  
   
plt.subplot(211)  
plt.plot(history.history['acc'])  
plt.plot(history.history['val_acc'])  
plt.title('model accuracy')  
plt.ylabel('accuracy')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left')  
   
 # summarize history for loss  
   
plt.subplot(212)  
plt.plot(history.history['loss'])  
plt.plot(history.history['val_loss'])  
plt.title('model loss')  
plt.ylabel('loss')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left')  
plt.show()
score = model.evaluate(X_test, Y_test, verbose=0)
# print score
print('Test score:', score[0])
print('Test accuracy:', score[1])

pred= model.predict(X_test,batch_size=1,verbose=1)
print pred
predict=np.reshape(pred,(52,10))
plt.plot(predict)
plt.show()
print pred
# model_json = model.to_json()

# with open("final_model.json","w") as json_file:
#  	json_file.write(model_json)
# model.save_weights("final_model_weights.h5", overwrite=True)
# print("Saved the Model to Disk")

