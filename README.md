# Masterarbeit

### Contents

This repository contains the annotation loop for the training data, the training data, saved models and results from training as well as a data exploration notebook.

### Folder Contents and Structure

```

├── graphs.ipynb                    contains figures code as well as annotation and training loop
├── annotated_data
    ├── cleaned_annotated_data_training.txt 
    ├── annotated_data_training.txt
├── data_exploration.ipynb          contains code for data exploration
└── saved_models
    ├──tokenizer                    trained tokenizer
    └──model                        trained model
    
```

### Training a model using jones

The models have been trained from a pre-trained model with the help of annotated data using the CoLi Jones-cluster. 
Training can be started by forwarding your local machine to the server

```
ssh -L 1235:localhost:1235 -J user@login.coli.uni-saarland.de user@jones-X  # replace X with desired server

```

and connecting to the forwarded adress notebook

```
ssh jupyter notebook --port:1235 --no-browser
```
