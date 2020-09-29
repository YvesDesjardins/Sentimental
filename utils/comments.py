import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.db import select_where_id, insert

table = "Comments"

def process_comments(post):
    comments = post.comments.list()
    top_comment = comments[0]
    records = select_where_id(table, top_comment.id)

    # insert if no records exist
    if len(records) == 0:
        options = "(id, post_id, author_id, score, body) VALUES (?, ?, ?, ?, ?)"
        data_tuple = (top_comment.id, top_comment.link_id, top_comment.author.id, top_comment.score, top_comment.body)
        insert(table, options, data_tuple)
    else:
        return
        # todo - might want to update existing?
