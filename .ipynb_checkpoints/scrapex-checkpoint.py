import praw
import pandas as pd
import datetime

reddit = praw.Reddit(user_agent = True, client_id = "TIS75MwWmLsOjqv91QCnag", 
                     client_secret = "Q0qiCAHZdR2CtqKpXhR6SKhJZ3uUUA", username = 'Low-Session-1247',
                     password = 'Kf9H17fBD***')

subreddit = reddit.subreddit('rap')
final_data = []
for post in subreddit.top(limit=10):
    data = [post.url, post.title, 
            post.selftext, 
            datetime.datetime.fromtimestamp(post.created_utc)]
    
    final_data.append(data)


df = pd.DataFrame(final_data)

print(df)

    #print("Link:", post.url)
    #print("Title:", post.title)
    #print("Selftext:", post.selftext)
    #print(f"Date:", datetime.datetime.fromtimestamp(post.created_utc))
    #print("-----------------------------------------")



 