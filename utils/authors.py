import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.db import select_where_id, insert

table = "Authors"

def process_author(author):
    author_id = author.id if hasattr(author, "id") else "invalid_id"
    records = select_where_id(table, author_id)

    # insert if no records exist
    if len(records) == 0:
        options = "(id, name) VALUES (?, ?)"
        data_tuple = (author_id, author.name )
        insert(table, options, data_tuple)
    else:
        return
        # todo - might want to update existing?
