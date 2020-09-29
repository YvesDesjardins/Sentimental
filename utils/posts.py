from services.db import get_db_client

db = get_db_client()

def process_post(post):
    print("Post -----------------")
    print(post.id)        # Output: the post's id
    print(post.title)     # Output: the post's title
    print(post.score)     # Output: the post's score
    print(post.selftext)  # Output: the post's selftext
    print(post.url)       # Output: the URL the post points to
                          # or the post's URL if it's a self post
