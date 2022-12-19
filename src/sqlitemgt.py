import sqlite3
from sqlite3 import Error

#Create schema if not exist
def setup_db(db_file):
    try:
        print("Creating schema...", end="")
        conn = sqlite3.connect(db_file)
        conn.execute("""CREATE TABLE IF NOT EXISTS txns (
            Id INTEGER PRIMARY KEY,
            Date TEXT,
            Txn REAL,
            User_id INTEGER);
            """)

        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            User_id INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT);
            """)
        conn.commit()
        print("done")
    except Error as e:
        print("error")
        print(e)
    finally:
        if conn:
            conn.close()

#Save transactions in db
def save_txns(df, db_file):

    print("Saving txns in db...", end="")

    query = "INSERT OR REPLACE INTO txns (Id,Date,Txn,User_id) VALUES"
    for index, row in df.iterrows():
        query = query + "({},'{}',{},{})".format(row['Id'],row['Date'],row['Transaction'],row['User_id'])
        if index != len(df)-1:
            query = query + ","
    query = query+';'

    try:
        conn = sqlite3.connect(db_file)
        conn.execute(query)
        conn.commit()
        print("done")
    except Error as e:
        print("error")
        print(e)
    finally:
        if conn:
            conn.close()

#Save users in db
def save_users(df, db_file):

    print("Saving users in db...", end="")
    query = "INSERT OR REPLACE INTO users (User_id,Name,Email) VALUES"
    for index, row in df.iterrows():
        query = query + "({},'{}','{}')".format(row['User_id'],row['Name'],row['Email'])
        if index != len(df)-1:
            query = query + ", " 
    query = query+';'

    try:
        conn = sqlite3.connect(db_file)
        conn.execute(query)
        conn.commit()
        print("done")
    except Error as e:
        print("error")
        print(e)
    finally:
        if conn:
            conn.close()