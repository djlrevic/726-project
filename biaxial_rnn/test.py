import pickle

import multi_training
import model
import main

#create instance of model
m = model.Model([300,300],[100,50], dropout=0.5)

#load pre-trained weights
m.learned_config = pickle.load(open( "models/final_learned_config.p", "rb" ) )

#load data
pcs = multi_training.loadPieces("music")

#generate new piece 
main.gen_adaptive(m,pcs,10,name="composition")
