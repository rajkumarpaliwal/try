
from typing import Text
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
# from create_table import connection
from security import authenticate, identity
# from user import UserRegister
# from test import connection

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

allname = []

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
        type=Text,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('password',
        type=Text,
        required=True,
        help="This field cannot be left blank!"
    )

    # @jwt_required()

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, allname), None) is not None:
            return {'message': "An User with this name '{}' already exists.".format(name)}

        data = User.parser.parse_args()

        user = {'name': name, 'email': data['email'], 'password':data['password']}
        allname.append(user)
        # return user,201
        return "User registeration seccessfuly",201

    @jwt_required()
    def delete(self, name):
        global allname
        allname = list(filter(lambda x: x['name'] != name,allname))
        return {'message': 'User deleted'}

    @jwt_required()
    def put(self, name):
        data = User.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        user = next(filter(lambda x: x['name'] == name, allname), None)
        if user is None:
            user = {'name': name, 'email': data['email'], 'password':data['password']}
            allname.append(user)
        else:
            user.update(data)
        return user

class Forgot(Resource):
    @jwt_required()
    def put(self, email):
      if next(filter(lambda x: x['email'] != email, allname), None) is not None:
        return {'message': "An User with this email '{}' isn't exists.".format(email)}
      else:
        data = User.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        user = next(filter(lambda x: x['email'] == email, allname), None)
        if user is None:
            user = {'email': data['email'], 'password':data['password']}
            allname.append(user)
        else:
            user.update(data)
        return "Update successfully"


class Login(Resource):
   def get(self, name,email,password):
     if   next(filter(lambda x: x['name'] == name, allname), None):
        if next(filter(lambda x: x['email'] == email, allname), None) is not None:
           if  next(filter(lambda x: x['password'] == password, allname), None) is not None:
            #  return {'message': "An User with this email '{}' isn't exists.".format(email)}
            user= next(filter(lambda x: x['name'] == name, allname), None)
            return {'user':user},200 if user else 404
           
            # return  '{} {} {}'.format(firstname, lastname, cellphone)
           else:
                return"Password is incorrect.."      
        else:
             return"email is incorrect.."   
     else:
          return"name is incorrect.."

class UserList(Resource):
    def get(self):
        return {'USERS': allname}

api.add_resource(User, '/user/<string:name>')
api.add_resource(UserList, '/allname')
api.add_resource(Forgot, '/forgot/<string:email>')
api.add_resource(Login, '/login/<string:name>/<string:email>/<string:password>')
# api.add_resource(index.html, '/allname')
# api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True) 
     # important to mention debug=True

# return flask.render_template('home.html')

# from typing import Text
# from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required, current_identity
# # from create_table import connection
# from security import authenticate, identity
# # from user import UserRegister
# # from test import connection
# # from flask.templating import render_template

# app = Flask(__name__)
# app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
# app.secret_key = 'jose'
# api = Api(app)

# jwt = JWT(app, authenticate, identity)

# allname = []

# class User(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('email',
#         type=Text,
#         required=True,
#         help="This field cannot be left blank!"
#     )

#     parser.add_argument('password',
#         type=Text,
#         required=True,
#         help="This field cannot be left blank!"
#     )

#     # @jwt_required()
    
#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, allname), None) is not None:
#             return {'message': "An User with this name '{}' already exists.".format(name)}

#         data = User.parser.parse_args()

#         user = {'name': name, 'email': data['email'], 'password':data['password']}
#         allname.append(user)
#         # return user,201
#         return "User registeration seccessfuly",201
#         # return flask.render_template('home.html')
#     @jwt_required()
#     def delete(self, name):
#         global allname
#         allname = list(filter(lambda x: x['name'] != name,allname))
#         return {'message': 'User deleted'}

#     @jwt_required()
#     def put(self, name):
#         data = User.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         user = next(filter(lambda x: x['name'] == name, allname), None)
#         if user is None:
#             user = {'name': name, 'email': data['email'], 'password':data['password']}
#             allname.append(user)
#         else:
#             user.update(data)
#         return user

# class Forgot(Resource):
#     @jwt_required()
#     def put(self, email,name):
#       if next(filter(lambda x: x['email'] != email, allname), None) is not None:
#         return {'message': "An User with this email '{}' isn't exists.".format(email)}
#       else:
#         data = User.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         user = next(filter(lambda x: x['email'] == email, allname), None)
#         if user is None:
#             user = {'email': data['email'], 'password':data['password']}
#             allname.append(user)
#         # else:
#         #     user.update(data)
#         return "Update successfully"


# class Login(Resource):
#    def get(self, name,email,password):
#      if   next(filter(lambda x: x['name'] == name, allname), None):
#         if next(filter(lambda x: x['email'] == email, allname), None) is not None:
#            if  next(filter(lambda x: x['password'] == password, allname), None) is not None:
#             #  return {'message': "An User with this email '{}' isn't exists.".format(email)}
#             user= next(filter(lambda x: x['name'] == name, allname), None)
#             return {'user':user},200 if user else 404
#            else:
#                 return"Password is incorrect.."      
#         else:
#              return"email is incorrect.."   
#      else:
#           return"name is incorrect.."

# class UserList(Resource):
#     def get(self):
#         return {'USERS': allname}

# api.add_resource(User, '/user/<string:name>')
# api.add_resource(UserList, '/allname')
# api.add_resource(Forgot, '/forgot/<string:email>')
# api.add_resource(Login, '/login/<string:name>/<string:email>/<string:password>')
# # api.add_resource(index.html, '/allname')
# # api.add_resource(UserRegister, '/register')

# if __name__ == '__main__':
#     app.run(debug=True) 