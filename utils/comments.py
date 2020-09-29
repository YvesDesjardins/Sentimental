from services.db import get_db_client

db = get_db_client()

def get_comments(post):
    print("Top Comment ----------")
    comment = post.comments[0]
    print(comment.id)
    print(comment.author)
    print(comment.score)
    print(comment.body)
