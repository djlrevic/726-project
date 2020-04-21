import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from pathlib import Path
from midi_dataset import MidiDataset

pd.options.display.width = 0  # use maximum terminal size
np.set_printoptions(precision=4)
if (not tf.executing_eagerly()):
    print('You are not running w/ eager execution. Try with TensorFlow version 2.1')

def get_uncompiled_model():
    inputs = keras.Input(shape=(None, 78, 2), name='note_state_matrix')
    x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
    x = layers.Dense(64, activation='relu', name='dense_2')(x)
    outputs = layers.Dense(tf.shape(inputs,0), name='predictions')(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model

def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(optimizer=keras.optimizers.RMSprop(learning_rate=1e-3),
                  loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
    return model

if __name__ == "__main__":
    dataset = MidiDataset()
    train_dataset = dataset.shuffle(buffer_size=4).batch(2)

    model = get_compiled_model()
    model.fit(train_dataset, epochs=1)


    # print(list(dataset.take(3).as_numpy_iterator()))



    #for feat, targ in dataset.take(5):
    # print(raw_midi[0])

    #midi = raw_midi[0]
    # extract features


# relevant example model code from https://www.tensorflow.org/tutorials/load_data/pandas_dataframe -

# target = df.pop('target')
#
# dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
#
# for feat, targ in dataset.take(5):
#     print ('Features: {}, Target: {}'.format(feat, targ))

#train_dataset = dataset.shuffle(len(df)).batch(1)

# def get_compiled_model():
#     model = tf.keras.Sequential([
#         tf.keras.layers.Dense(10, activation='relu'),
#         tf.keras.layers.Dense(10, activation='relu'),
#         tf.keras.layers.Dense(1)
#     ])
#
#     model.compile(optimizer='adam',
#                   loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
#                   metrics=['accuracy'])
#     return model
#
# model = get_compiled_model()
# model.fit(train_dataset, epochs=15)

# with ZipFile("maestro-v2.0.0-midi.zip", 'r') as zip:
#    for info in zip.infolist():

# net = Net()
# net.save_weights('easy_checkpoint')

# define parameters

# class Net(tf.keras.Model):
#   """A simple linear model."""

#   def __init__(self):
#     super(Net, self).__init__()
#     self.l1 = tf.keras.layers.Dense(5)

#   def call(self, x):
#     return self.l1(x)

