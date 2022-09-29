# Masterarbeit

### Contents

This repository contains the code for my Master's Thesis.

### Requirements
The required packages can be installed with the help of the requirements.txt

```
pip install -r requirements.txt
```

### Folder Contents and Structure
The are 5 notebooks used for training the model an annotating the data
* BERTcasedTrain.ipynb
    * contains BERT Base Cased Classifier for Topic, Opinion and Sentiment
* active_learning.ipynb
    * contains annotation loop for active learning sampled comments
* data_exploration.ipynb
    * contains data manipulation methods with markdown added for explanations
* sentiment_bert.ipynb
    * contains training for German Sentiment BERT Model
* graphs.ipynb
    * contains all methods for creating figures of Thesis
* UseModelPredict.ipynb
   * contains Notebook for prediciting with trained model
    
    
Regarding the data annotated, the main files where annotations can be found are:
* annotated_data_with_users_and_al_cleaned2check_final_topics.csv
    * This contains all of the annotated data with Topic Comment, Article, Sentiment and Opinion
* annotated_data_with_users_and_al_cleaned2check_article.csv
    * This contains the article headers as comments needed for training an Article Topic classifier

The remaining files in the ``` annotated_data``` folder are needed for executing graphs.ipynb, etc.





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
