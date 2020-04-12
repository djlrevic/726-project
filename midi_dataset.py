import midi
import numpy as np
import pandas as pd
import tensorflow as tf

from pathlib import Path

class MidiDataset(tf.data.Dataset):
    def _midiFileToData(self, file: Path) -> tf.Tensor:
        m = midi.read_midifile(file)
        print(f"Reading {file}:\n\t"
              f"Format:{m.format}\n\t"
              f"Resolution:{m.resolution}\n\t"
              f"TickRelative:{m.tick_relative}\n")
        return tf.zeros((1,))

    def _generator(self, num_samples):
        data_folder = Path("maestro-v2.0.0")
        csv = pd.read_csv(data_folder/"maestro-v2.0.0.csv")
        print(csv.describe())
        print(csv.head(2))

        filenames = csv['midi_filename'].head(1)
        midi_files = [f for f in filenames]

        for f in midi_files:
            # Reading data (line, record) from the file
            yield self._midiFileToData(f)

    def __new__(cls, num_samples=3):
        return tf.data.Dataset.from_generator(
            cls._generator,
            output_types=tf.dtypes.int64,
            output_shapes=(1,),
            args=(num_samples,)
        )
