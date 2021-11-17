import re
from typing import List
from dataloader import DataLoader
import numpy as np
import torch
from tqdm import tqdm
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.metrics import ConfusionMatrixDisplay, f1_score
import matplotlib.pyplot as plt

class SentimentModel():
    def __init__(self, model_name: str):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.clean_chars = re.compile(r'[^A-Za-züöäÖÜÄß ]', re.MULTILINE)
        self.clean_http_urls  = re.compile(r'https*\\S+', re.MULTILINE)
        self.clean_at_mentions = re.compile(r'@\\S+', re.MULTILINE)

    def predict_sentiment(self, texts: List[str])-> List[str]:
            texts = [self.clean_text(text) for text in texts]
            # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
            input_ids = self.tokenizer(texts, padding=True, truncation=True, add_special_tokens=True)
            input_ids = torch.tensor(input_ids["input_ids"])

            with torch.no_grad():
                logits = self.model(input_ids)    

            label_ids = torch.argmax(logits[0], axis=1)

            labels = [self.model.config.id2label[label_id] for label_id in label_ids.tolist()]
            return labels

    def replace_numbers(self,text: str) -> str:
                return text.replace("0"," null").replace("1"," eins").replace("2"," zwei").replace("3"," drei").replace("4"," vier").replace("5"," fünf").replace("6"," sechs").replace("7"," sieben").replace("8"," acht").replace("9"," neun")         

    def clean_text(self,text: str)-> str:    
            text = text.replace("\
    ", " ")        
            text = self.clean_http_urls.sub('',text)
            text = self.clean_at_mentions.sub('',text)        
            text = self.replace_numbers(text)                
            text = self.clean_chars.sub('', text) # use only text chars                          
            text = ' '.join(text.split()) # substitute multiple whitespace with single whitespace   
            text = text.strip().lower()
            return text


def get_labels(model_name, annotations_file):

    model = SentimentModel(model_name)

    myfile = DataLoader(annotations_file)

    meine_texts = myfile.load_data_texts()

    mypredictions = model.predict_sentiment(meine_texts)

    print("Hi hier", mypredictions)

    labels_opinion = myfile.load_data_labels_opinion()

    labels_sentiment = myfile.load_data_labels_sentiment()

    return mypredictions, labels_opinion, labels_sentiment, myfile



def get_figures(labels, predictions, title, save_name, myfile, verbose = False):
        
    ConfusionMatrixDisplay.from_predictions(labels, predictions)

    figure = plt.gcf()

    plt.title(title)

    figure.savefig(save_name)

    if verbose:
        plt.show()
        print(title)
        myfile.print_ratio(labels, predictions)

if __name__ == "__main__":
    mypredictions, labels_opinion, labels_sentiment, myfile = get_labels("oliverguhr/german-sentiment-bert", "Annotation_Opinion_Sentiment.txt")

    get_figures(labels_sentiment, mypredictions, "Confusion Matrix Sentiment Maskenpflicht", "Maskenpflicht_sentiment", myfile, True)

    get_figures(labels_opinion, mypredictions, "Confusion Matrix Opinion Maskenpflicht", "Maskenpflicht_opinion", myfile, True)











