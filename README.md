# Masterarbeit

### Contents

This repository contains the code for my Master Thesis.



### Folder Contents and Structure
The are 5 notebooks used for training the model an annotating the data
* base_cased_classifier.ipynb
    * contains BERT Base Cased Classifier for Topic, Opinion and Sentiment
* active_learning.ipynb
    * contains annotation loop for active learning sampled comments
* data_exploration.ipynb
    * contains data manipulation methods with markdown added for explanations
* sentiment_bert.ipynb
    * contains training for German Sentiment BERT Model
* graphs.ipynb
    * contains all methods for creating figures of Thesis
    
    
Regarding the data annotated, the main files where annotations can be found are:
* annotated_data_with_users_and_al_cleaned2check_final_topics.csv
    * This contains all of the annotated data with Topic Comment, Article, Sentiment and Opinion
* annotated_data_with_users_and_al_cleaned2check_article.csv
    * This contains the article headers as comments needed for training an Article Topic classifier
* data_augment_400_positive.csv
    *
```  
├── annotated_data
    ├── cleaned_annotated_data_training.txt 
    ├── annotated_data_training.txt
    ├──
    ├──vali_agreement.txt                           Annotation Samples for Vali used in IAA
    ├──svens_agreement.txt                          Annotation Samples for Sven used in IAA
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
