import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE user (id int, username text, password text)"
cursor.execute(create_table)

users = [
    (1, 'jose', 'asdf'),
    (2, 'rodolf', 'asdf'),
    (3, 'anne', 'xyz')
]
insert_query = "INSERT INTO user VALUES (?, ?, ?)"

cursor.executemany(insert_query,users)
connection.commit()

select_query = "SELECT * FROM user"
for row in cursor.execute(select_query):
    print(row)
connection.close()