import os
from keras.utils import plot_model
os.environ['KERAS_BACKEND'] = 'theano'
from keras.models import model_from_json
import theano

json_file = open('new1_model.json', 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("new2_model_weights.h5")


for i in model.layers:
    theano.printing.debugprint(i.input)
    theano.printing.debugprint(i.output)