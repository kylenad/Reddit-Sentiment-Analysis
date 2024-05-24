# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import numpy as np
from scipy.special import softmax
import re
import emoji


def preprocess(text):
    new_text = re.sub(r'https?://\S+|www\.\S+', '', text)

    new_text = re.sub(r'\bu/[\w-]+', 'user', text)

    new_text = emoji.replace_emoji(text, replace='')

    return new_text


def processData(model, tokenizer):
    df = pd.read_csv("redditData.csv")
    df['features'] = df['1'] + ' ' + df['2']
    df['features'] = df['features'].astype(str)

    df['features'] = df['features'].apply(preprocess)
    
    results = []
    for text in df['features']:
        #tokenize data for ML model
        encoded_input = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
        with torch.no_grad():
            output = model(**encoded_input)
            scores = output.logits.detach().numpy()[0]
            probabilities = softmax(scores)
            sentiment = np.argmax(probabilities)
            results.append({'text': text, 'sentiment': sentiment, 'probability': probabilities[sentiment]})

    results_df = pd.DataFrame(results)
    return results_df



if __name__ == "__main__":
    #Load model and tokenizer
    #Transfer learning
    #Model is trained on examples pulled from Twitter
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
    model.eval()

    results = processData(model, tokenizer)

    results.to_csv("results.csv", index = False)
    
    