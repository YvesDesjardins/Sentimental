import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.db import select_where_id, insert

table = "Comments"

def process_comments(post):
    post.comments.replace_more(limit=10)
    comments = post.comments.list()
    for comment in comments:
      records = select_where_id(table, comment.id)

      # insert if no records exist
      if len(records) == 0:
          options = "(id, post_id, author_id, score, body) VALUES (?, ?, ?, ?, ?)"
          data_tuple = (comment.id, post.id, comment.author.id, comment.score, comment.body)
          insert(table, options, data_tuple)
      else:
          return
          # todo - might want to update existing?
