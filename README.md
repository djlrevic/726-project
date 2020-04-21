# 716 Project - Frisson - Generating Music With LSTMs

Three projects used to generate music for our 726 report are included in this repo, and our inital unfinished attempt at implementing our own, which turned into an exploration of Tensorflow's Dataset and midi processing (tf-dataset-midi-processing).


The best results (midi files) are in `biaxial_rnn/output`. The other two have some example midi files in the roots.


## Models used for training:

biaxial_rnn - [Daniel Johnson's Generating Polyphonic Music Using Tied Parallel Networks](https://www.cs.hmc.edu/~ddjohnson/tied-parallel/)

basic_lstm - [Christopher  Olah's Understanding  lstm  networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

bidirectional_lstm - [Alex Issa's Generating Original Classical Music with an LSTM Neural Network and Attention](https://medium.com/@alexissa122/generating-original-classical-music-with-an-lstm-neural-network-and-attention-abf03f9ddcb4)


## Use

To train or generate, content must be added to the `midi_files` folder, and then the relevant train/generate (lstm-`name`.py/predict-`name`.py) can be run. `biaxial_rnn` contains the weights needed, the others do not (much larger and worse performance with our level of training)


## Dependencies:
Python 3.6

| Package | Version |
| --- | --- |
| tensorflow           | 1.15.0 |
| pandas               | 0.24.2 |
| numpy                | 1.18.1 |
| Keras                | 2.3.1 |
| keras-self-attention | 0.42.0 |
| music21              | 5.7.2 |

