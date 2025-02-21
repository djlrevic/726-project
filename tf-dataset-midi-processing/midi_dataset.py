import midi
import pandas as pd
import tensorflow as tf
import time

import midi_musical_matrix as mmm

from pathlib import Path

class MidiDataset(tf.data.Dataset):
    @staticmethod
    def _generator():
        data_folder = Path("maestro-v2.0.0")
        csv = pd.read_csv(
            data_folder/"maestro-v2.0.0.csv",
            usecols=['canonical_composer', 'canonical_title', 'year', 'midi_filename', 'duration']
        )

        midi_files = [f for f in csv['midi_filename']]

        for f in midi_files:
            # Reading data (line, record) from the file
            yield mmm.midiToNoteStateMatrix(str(data_folder/f))

    def __new__(cls, num_samples=3):
        return tf.data.Dataset.from_generator(
            cls._generator,
            output_types=tf.dtypes.int64,
            output_shapes=(None, 78, 2),
            args=None
        )

def benchmark(dataset, num_epochs=2):
    start_time = time.perf_counter()
    for epoch_num in range(num_epochs):
        print(f"Epoch: {epoch_num}")
        count=0
        for sample in dataset:
            count += 1
            print(f"Sample: {count}")
            # Performing a training step
            time.sleep(0.01)
    print("Execution time:", time.perf_counter() - start_time)

if __name__=="__main__":
    benchmark(MidiDataset())