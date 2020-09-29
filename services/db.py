import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

def get_db_client():
    return sqliteConnection

def close_db_connection():
    cursor.close()
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
