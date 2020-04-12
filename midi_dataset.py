import pretty_midi
import numpy as np
import pandas as pd
import tensorflow as tf

from pathlib import Path

class MidiDataset(tf.data.Dataset):
    @staticmethod
    def _midiFileToData(file: Path) -> tf.Tensor:
        m = pretty_midi.PrettyMIDI(str(file))
        piano_roll = m.instruments[0].get_piano_roll()
        print(piano_roll)
        # print(f"Reading {file}:\n\t"
        #       f"Format:{m.format}\n\t"
        #       f"Resolution:{m.resolution}\n\t"
        #       f"TickRelative:{m.tick_relative}\n")
        return tf.convert_to_tensor(piano_roll)

    @staticmethod
    def _generator():
        data_folder = Path("maestro-v2.0.0")
        csv = pd.read_csv(
            data_folder/"maestro-v2.0.0.csv",
            usecols=['canonical_composer', 'canonical_title', 'year', 'midi_filename', 'duration']
        )

        print(csv.describe())
        print(csv.head(2))

        filenames = csv['midi_filename'].head(1)
        midi_files = [f for f in filenames]

        for f in midi_files:
            # Reading data (line, record) from the file
            yield MidiDataset._midiFileToData(data_folder/f)

    def __new__(cls, num_samples=3):
        return tf.data.Dataset.from_generator(
            cls._generator,
            output_types=tf.dtypes.int64,
            output_shapes=(128, None),  # right now just midi 1-128
            args=None
        )
