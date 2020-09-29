import praw
from dotenv import load_dotenv
load_dotenv()
import os

def get_reddit_client():
  return praw.Reddit(client_id=os.getenv("CLIENT_ID"),
      client_secret=os.getenv("CLIENT_SECRET"),
      user_agent="testscript by u/readdit-bot",
      username=os.getenv("USERNAME"),
      password=os.getenv("PASSWORD")
  )
