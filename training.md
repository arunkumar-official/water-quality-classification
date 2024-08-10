### Model Training Info

all training related files are in Training Directory.

#### Folder image_classify
This folder contains N(number of labels) folders. (for this project 2 folders, ie. clean and dirty) 
These data is used to Train the model.

#### Folder test
This folder contains N(number of labels) folders. (for this project 2 folders, ie. clean and dirty)
These data is used to validate the model, to understand how model generalise its training knowledge. 

#### train.py and water_quality_prediction.ipynb
These files are same. This is training code where we define our CNN architecture using Tensorflow framework.
Here we define:
1.loss function
2.optimiser
3.metrics to validate
4.number of epoch
5.number of steps in each epoch

#### After training:
after training has done we will export the model to .pkl format which can be later used by deep learning inference server.
idealy we should have ```tensorflow or pytorch format```, but here model is small so .pkl format is used.
also ```.onnx``` format can be used to serve the model efficiently.