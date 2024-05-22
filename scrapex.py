import praw
import pandas as pd

reddit = praw.Reddit(user_agent = True, client_id = "id", 
                     client_secret = "key", username = 'username',
                     password = 'password')

url = "https://www.reddit.com/r/rap/comments/1cyaukk/if_we_compared_every_rapper_to_a_nba_player_who/"
post = reddit.submission(url=url)

print(post.selftext)

for comment in post.comments:
    print(comment.body)