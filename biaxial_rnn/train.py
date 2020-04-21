import pickle

import multi_training
import model
import main

#create instance of model
m = model.Model([300,300],[100,50], dropout=0.5)

#load data
pcs = multi_training.loadPieces("music")

multi_training.trainPiece(m, pcs, 10000)

pickle.dump( m.learned_config, open( "output/trained_model.p", "wb" ) )

#generate new piece 
main.gen_adaptive(m,pcs,10,name="trained_composition")