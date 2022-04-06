# Masterarbeit

### Contents

This repository contains the annotation loop for the training data, the training data, saved models and results from training as well as a data exploration notebook.

### Folder Contents and Structure

```
├── accuracy_loss                   contains .csv files for plotting loss and accuracy for trained models
    ├──my_accuracy_loss.csv         
├── annotated_data
    ├── cleaned_annotated_data_training.txt 
    ├── annotated_data_training.txt
├── graphs.ipynb                    contains figures code as well as annotation and training loop
├── sent_analysis.py                pretrained model classifier
├── data_exploration.ipynb          contains code for data exploration
└── saved_models
    ├──tokenizer                    trained tokenizer
    └──model                        trained model
    
```

### Training a model using jones on local machine

The models have been trained from a pre-trained model with the help of annotated data using the CoLi Jones-cluster. 
Training can be started by forwarding your local machine to the CoLi-server

```
ssh -L 1235:localhost:1235 -J user@login.coli.uni-saarland.de user@jones-X  # replace X with desired server

```

starting a notebook on the server 

```
ssh -J user@login.coli.uni-saarland.de user@jones-X jupyter notebook --port=1235 --no-browser
```

and connecting to your machine using

```
localhost:1235 # use port specified in step 2
```

The training notebook contains the training loop that is needed for training the model.
