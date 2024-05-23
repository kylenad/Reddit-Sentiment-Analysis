import praw
import pandas as pd
import datetime

def compileData():
    reddit = praw.Reddit(user_agent = True, client_id = "id", 
                        client_secret = "", username = '',
                        password = 'password')

    subreddit = reddit.subreddit('rap')
    final_data = []
    for post in subreddit.new(limit=1000):
        data = [post.url, post.title, 
                post.selftext, 
                datetime.datetime.fromtimestamp(post.created_utc)]
        
        final_data.append(data)


    df = pd.DataFrame(final_data)

    df.to_csv("redditData", index = False)


if __name__ == "__main__":
    compileData()
   



 