from services.reddit import get_reddit_client
from utils.posts import process_post
from utils.comments import process_comments
from services.db import close_db_connection

def run():
  reddit = get_reddit_client()
  subreddit = reddit.subreddit("wallstreetbets")
  # make sure to increase praw's rate limit in env/lib/praw/praw.ini, 45 has worked for me
  posts = subreddit.hot(limit=100)

  print("Updating DB and preping model, this may take a minute or two")
  for post in posts:
      process_post(post)
      process_comments(post)

  close_db_connection()

if __name__ == "__main__":
    run()
