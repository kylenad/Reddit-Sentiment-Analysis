import praw
import requests
import datetime

def fetch_posts_from_pushshift(subreddit, start_time, end_time):
    url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&after={start_time}&before={end_time}&size=100"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        return [post['id'] for post in posts['data']]
    else:
        return []

def date_to_timestamp(year, month, day):
    return int(datetime.datetime(year, month, day, 0, 0).timestamp())

# Define the date range
# Fall 2024 starts on September 23, 2024 and ends December 21, 2024
# Note: You mentioned "May 2024," assuming you meant starting from May 1, 2024 to Fall
start_date = date_to_timestamp(2024, 2, 1)  
end_date = date_to_timestamp(2024, 4, 21)  

# Fetch post IDs from Pushshift for the subreddit "rap"
post_ids = fetch_posts_from_pushshift('rap', start_date, end_date)

# Initialize PRAW with your details
reddit = praw.Reddit(client_id="TIS75MwWmLsOjqv91QCnag",
                     client_secret="Q0qiCAHZdR2CtqKpXhR6SKhJZ3uUUA",
                     user_agent="script:subreddit_scraper:v1.0 (by u/Low-Session-1247)",
                     username='Low-Session-1247',
                     password='Kf9H17fBD***')

# Use PRAW to fetch detailed data for each post using the post IDs
for post_id in post_ids:
    submission = reddit.submission(id=post_id)
    print(f"Title: {submission.title}")
    print(f"Selftext: {submission.selftext}")
    print(f"Date: {datetime.datetime.fromtimestamp(submission.created_utc)}")
    print("-" * 40)

# Note: Make sure you handle rate limits and use appropriate error handling in production code.