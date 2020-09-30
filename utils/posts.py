import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.db import select_where_id, insert
from utils.authors import process_author

table = "Posts"

def process_post(post):
    records = select_where_id(table, post.id)
    author_id = post.author.id if hasattr(post.author, "id") else "invalid_id"

    # insert if no records exist
    if len(records) == 0:
        options = "(id, author_id, title, score, selftext, url) VALUES (?, ?, ?, ?, ?, ?)"
        data_tuple = (post.id, author_id, post.title, post.score, post.selftext, post.url)
        insert(table, options, data_tuple)
    else:
        return
        # todo - might want to update existing?
