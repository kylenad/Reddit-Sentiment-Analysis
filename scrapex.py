import praw
import pandas as pd
import datetime

reddit = praw.Reddit(user_agent = True, client_id = "id", 
                     client_secret = "key", username = 'user',
                     password = 'password')

subreddit = reddit.subreddit('rap')
for post in subreddit.top(limit=10):
    print("Link:", post.url)
    print("Title:", post.title)
    print("Selftext:", post.selftext)
    print(f"Date:", datetime.datetime.fromtimestamp(post.created_utc))
    print("-----------------------------------------")



 