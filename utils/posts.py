import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.db import select_where_id, insert

table = "Posts"

def process_post(post):
    records = select_where_id(table, post.id)

    # insert if no records exist
    if len(records) == 0:
        options = "(id, author_id, title, score, selftext, url) VALUES (?, ?, ?, ?, ?, ?)"
        data_tuple = (post.id, post.author.id, post.title, post.score, post.selftext, post.url)
        insert(table, options, data_tuple)
    else:
        return
        # todo - might want to update existing?
