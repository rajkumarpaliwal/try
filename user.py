import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from  flask_restful import Resource,reqparse
class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        if row :
            user = cls(*row)

        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls,id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result=cursor.execute(query,(id,))
        row=result.fetchone()
        if row :
            user = cls(*row)

        else:
            user = None

        connection.close()
        return user   

# class UserRegister(Resource):

#     parser =reqparse.RequestParser()
#     parser.add_argument('email',
#     type=str,
#     required=True,
#     help="This fild can't be blank.."
#   )
#     parser =reqparse.RequestParser()
#     parser.add_argument('password',
#     type=str,
#     required=True,
#     help="This fild can't be blank.."
#   )

#     def post(self):
#         data=UserRegister.parser.parse_args()

#         connection = sqlite3.connect('data.db')
#         cursor=connection.cursor

#         query ="INSERT INTO users VALUES (NULL,?,?)"
#         cursor.execute(query,(data['email'],data['password']))

#         connection.commit()
#         connection.close()

#         return{"message": "User create successfully.."},201