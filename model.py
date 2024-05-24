# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import numpy as np
from scipy.special import softmax
import re
import emoji



#Load model and tokenizer
#Transfer learning
#Model is trained on examples pulled from Twitter
def model(data):
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
    model.eval()



def preprocess(text):
    new_text = re.sub(r'https?://\S+|www\.\S+', '', text)

    new_text = re.sub(r'\bu/[\w-]+', 'user', text)

    new_text = emoji.replace_emoji(text, replace='')

    return new_text


def processData():
    df = pd.read_csv("redditData.csv")
    df['features'] = df['1'] + ' ' + df['2']
    df['features'] = df['features'].astype(str)

    df['features'] = df['features'].apply(preprocess)
    return df['features']
    



if __name__ == "__main__":
    #model()
    data = processData()
    print(data)
    