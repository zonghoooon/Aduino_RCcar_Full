from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
#import pandas as pd
import tensorflow as tf
#import pickle
new_model = tf.keras.models.load_model('model1.h5')

# 모델 구조를 출력합니다
new_model.summary()