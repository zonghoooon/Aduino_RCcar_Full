# Copyright Reserved (2020).
# Donghee Lee, Univ. of Seoul
#
__author__ = 'will'

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
#from sklearn.model_selection import train_test_split

import numpy as np
#import pandas as pd
import tensorflow as tf
#import pickle
from get_image_data import *

class DNN_Driver():
    def __init__(self):
        self.trX = None
        self.trY = None
        self.teX = None
        self.teY = None
        self.model = None

    def tf_learn(self):
        self.model = tf.keras.models.load_model('model1.h5') #model browse
#         self.trX, self.trY = get_training_data()
#         self.teX, self.teY = get_test_data()
# 
#         seed = 0
#         np.random.seed(seed)
#         tf.random.set_seed(seed)
# 
#         self.model=Sequential()
#         self.model.add(Dense(512, input_dim=np.shape(self.trX)[1], activation='relu'))
#         self.model.add(Dense(64, activation='relu'))
#         self.model.add(Dense(1))
# 
#         self.model.compile(loss='mean_squared_error', optimizer='adam')
# 
#         self.model.fit(self.trX, self.trY, epochs=32, batch_size=5)
# #         180 10
#         self.model.save('model2.h5')
        return

    def predict_direction(self, img):
        print(img.shape)
#        img = np.array([np.reshape(img,img.shape**2)])
        ret =  self.model.predict(np.array([img]))
        return ret

    def get_test_img(self):
        img = self.teX[10]
        return img

        