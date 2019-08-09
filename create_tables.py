import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS user (id integer primary key, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS item (id integer primary key, name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()