import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.db import select_where_id, insert

table = "Authors"

def process_author(author):
    records = select_where_id(table, author.id)

    # insert if no records exist
    if len(records) == 0:
        options = "(id, name) VALUES (?, ?)"
        data_tuple = (author.id, author.name )
        insert(table, options, data_tuple)
    else:
        return
        # todo - might want to update existing?
