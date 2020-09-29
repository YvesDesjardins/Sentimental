from services.reddit import get_reddit_client
from utils.posts import process_post
from utils.comments import get_comments
from services.db import close_db_connection

reddit = get_reddit_client()
subreddit = reddit.subreddit("wallstreetbets")
posts = subreddit.hot(limit=10)

print("Updating DB and preping model, this may take a minute or two")
for post in posts:
    process_post(post)
    get_comments(post)

close_db_connection()
