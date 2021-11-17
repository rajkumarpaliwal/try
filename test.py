import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('data.db')

cursor =connection.cursor()
create_table="CREATE TABLE users(id int, username text,password text)"
cursor.execute(create_table)

user=(1,'ram','ram')
insert_query ="INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)
users=[
    (2,'rajkumar','rajkumar'),
    (3,'hitesh','hitesh')
]
cursor.executemany(insert_query,users)

select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# connection.session.add(row)
connection.commit()
connection.close()


# import sqlite3
# from sqlite3.dbapi2 import Cursor

# connection = sqlite3.connect('data.db')

# cursor =connection.cursor()
# create_table="CREATE TABLE users(name text, username text,password text)"
# cursor.execute(create_table)

# user=('ram','ram@gmail','AAAA')
# insert_query ="INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query,user)
# users=[
#     ('raj','raj@gmail','BBBB'),
#     ('rk','rk@gmail','CCCC')
# ]
# cursor.executemany(insert_query,users)

# select_query="SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)
   
# connection.commit()
# connection.close()


# import sqlite3
# from sqlite3.dbapi2 import Cursor

# connection = sqlite3.connect('data.db')

# cursor =connection.cursor()
# create_table="CREATE TABLE users(id int, username text,password text)"
# cursor.execute(create_table)

# user=(1,'RK','AAAA')
# insert_query ="INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query,user)
# users=[
#     (2,'RAM','BBBB'),
#     (3,'SHAYAM','CCCC')
# ]
# cursor.executemany(insert_query,users)

# select_query="SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

# connection.session.add(row)
# connection.commit()
# connection.close()


# import sqlite3
# from sqlite3.dbapi2 import Cursor

# connection = sqlite3.connect('data.db')

# cursor =connection.cursor()
# create_table="CREATE TABLE users(name text, username text,password text)"
# cursor.execute(create_table)

# user=('ram','ram@gmail','AAAA')
# insert_query ="INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query,user)
# users=[
#     ('raj','raj@gmail','BBBB'),
#     ('rk','rk@gmail','CCCC')
# ]
# cursor.executemany(insert_query,users)

# select_query="SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)
   
# connection.commit()
# connection.close()