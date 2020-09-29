import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

def close_db_connection():
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

def select_where_id(table, id):
    try:
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from %s where id = ?""" % table
        cursor.execute(sqlite_select_query, (id,))
        records = cursor.fetchall()

        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

def insert(table, options, data_tuple):
    try:
        cursor = sqliteConnection.cursor()
        sqlite_insert_with_param = """INSERT INTO %(table)s %(options)s;""" % {"table": table, "options": options}

        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
