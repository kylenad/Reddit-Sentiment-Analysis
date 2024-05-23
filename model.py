# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

data = pd.read_csv("redditData.csv")