import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from keras.utils import to_categorical
from keras import models
from keras import layers

from keras.datasets import imdb
# download the 'imdb' set which was downloaded default by the Keras management authority
(train_data, train_targets),(test_data, test_targets)= imdb.load_data(num_words=10000)


