import pandas as pd
from tqdm.notebook import tqdm
from ntscraper import Nitter

scraper = Nitter()

tweets = scraper.get_tweets('#Drake', mode = 'hashtag', number = 5)
print(tweets)




