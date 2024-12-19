import praw
import time

# Assuming you have already set up the Reddit client (praw instance)
reddit = praw.Reddit( username='Good-Improvement1044',
                      password="Rihaan123@",
                     client_id='zkCvo1xhyAVwxmNb8-L7bw', 
                     client_secret='TuwY0y7QbUOWTuoC0hXXaqa786UJDw', 
                     user_agent='u/Good-Improvement1044')

def post_to_reddit(subreddit, title, url):
    try:
        # Submit the post to the specific subreddit
        submission = reddit.subreddit(subreddit).submit(title, url=url)
        
        # After successful post, print the link to the post
        print(f"Post successfully created! You can view it here: {submission.url}")
    
    except Exception as e:
        print(f"Error posting to Reddit: {e}")

# Example usage
subreddit = "learnpython"  # replace with your target subreddit
title = "Learning Python is fun!"  # replace with your post title
url = "http://example.com"  # replace with your URL

# Call the function to post
post_to_reddit(subreddit, title, url)

