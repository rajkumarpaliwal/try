# import sqlite3
# # from sqlite3.dbapi2 import Cursor
# # from typing import Collection

# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()

# create_table ="CREATE TABLE IF NOT EXISTS users (name STRING PRIMARY KEY, username text,password text)"
# cursor.execute(create_table)

# create_table ="CREATE TABLE IF NOT EXISTS items (name text, price real)"
# cursor.execute(create_table)


# connection.commit()

# connection.close()
 
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
        # return '<User %r>' % self.username1