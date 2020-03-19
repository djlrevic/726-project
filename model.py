import midi
import pandas as pd
import tensorflow as tf

from pathlib import Path

if (not tf.executing_eagerly()):
    print('You are not running w/ eager execution. Try with TensorFlow version 2.1')


if __name__ == "__main__":
    pd.options.display.width = 0  # use maximum terminal size

    data_folder = Path("maestro-v2.0.0")
    csv = pd.read_csv(data_folder/"maestro-v2.0.0.csv")
    print(csv.describe())
    print(csv.head(5))

    filenames = csv['midi_filename'].head(3)
    raw_midi = [midi.read_midifile(data_folder/f) for f in filenames]

    print(raw_midi[0])

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

