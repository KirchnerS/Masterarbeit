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

model = SentimentModel(model_name = "oliverguhr/german-sentiment-bert")

maskenpflicht = DataLoader("sample_annotation_maskenpflicht.txt" )

meine_texts_maskenpflicht = maskenpflicht.load_data_texts()

predictions_maskenpflicht = model.predict_sentiment(meine_texts_maskenpflicht)

labels_maskenpflicht = maskenpflicht.load_data_labels()

maskenpflicht.print_ratio(labels_maskenpflicht, predictions_maskenpflicht)
        
ConfusionMatrixDisplay.from_predictions(labels_maskenpflicht, predictions_maskenpflicht)

plt.show()

print(f1_score(labels_maskenpflicht, predictions_maskenpflicht, average="macro"))











