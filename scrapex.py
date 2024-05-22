import pandas as pd
from tqdm.notebook import tqdm
from ntscraper import Nitter

scraper = Nitter()

tweets = scraper.get_tweets('Drake', mode = 'hashtag', number = 5)

final_tweets = []
for tweet in tweets['tweets']:
    data = [tweet['link'], tweet['text'], tweet['date']]
    final_tweets.append(data)

df = pd.DataFrame(final_tweets, columns =['link', 'text', 'date'])






