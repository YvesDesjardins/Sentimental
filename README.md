# Sentimental
WSB sentiment analysis

## Details
Uses PRAW(https://github.com/praw-dev/praw) to scrape /r/wallstreetbets and pull 100 "hot" DDs from the previous week. From there the data is filtered, parsed and stored in SQLite db before being handed off for analysis using NLTK for sentiment analysis.

The model being used is VADER (https://github.com/cjhutto/vaderSentiment), originally an attempt was made to utilize a custom model but VADER outperformed in the majority of instances.

## Instructions
- pip(3) install -r requirements.txt
- Rename .env.public to .env and populate with your information
- python(3) main.py
- If you have issues with results/running, try increasing the timeout and ratelimits for PRAW
  - Increase PRAW's timeout in env/lib/praw/praw.ini, 45 has worked for me along with ratelimit 10

## Stack
- Python
- SQLite3
- PRAW
- NLTK

## Disclosure
As data is being pulled and stored from Reddit (and especially Wallstreet Bets) there will likely be some comments that are rather distateful/inappropriate. I do not agree with or support any opinions or comments that might be included in the DB unless I outright state so here. This is just for a fun project so please treat it as such :).

## Future additions
- User rating system based on track record
- FE to navigate details
- Make the code not shit
- Perform sentiment analysis off of stored posts + comments
