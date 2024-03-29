# import sqlite3
# from sqlite3.dbapi2 import Connection, connect
# # from typing_extensions import Required
# # from sqlite3.dbapi2 import Connection, Cursor
# from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required


# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#                         type=float,
#                         required=True,
#                         help="This field cannot be left blank!"
#                         )

#     @jwt_required()
#     def get(self, name):
#       item = self.find_by_name(name)
#       if item:
#           return item
#       return {'message': 'Item not found'}, 404

#     @classmethod
#     def find_by_name(cls,name):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "SELECT * FROM items WHERE name=?"
#         result = cursor.execute(query, (name,))
#         row = result.fetchone()
#         connection.close()

#         if row:
#             return {'item': {'name': row[0], 'price': row[1]}}
#         # return {'message': 'Item not found'}, 404

#     def post(self, name):
#         if self.find_by_name(name):
#             return{'message': "An item with name '{}' already exists.".format(name)}, 400

#         data = Item.parser.parse_args()

#         item = {'name': name, 'price': data['prise']}
       
#         try:
#             self.insert(item)

#         except:
#             return {"Message": "An error occurred inserting the item."},500
            
#         return item, 201
#     @classmethod
#     def insert(cls,item):
#         connection = sqlite3.connect('data,db')
#         cursor = connection.cursor()

#         query ="INSERT INTO item VALUES (?,?)"
#         cursor.execute(query,(item['name'],item['price']))

#         connection.commit()
#         connection.close()
#         return item, 201

#     def delete(self, name):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query ="DELETE FROM item WHERE name=?"
#         cursor.execute(query,(name,))

#         connection.commit()
#         connection.close()
#         return {'message': 'Item deleted'}

#     def put(self, name):
#         parser = reqparse.RequestParser()
#         parser.add_argument('price',
#                             type=float,
#                             required=True,
#                             help='This field connot be left blank!'
#                             )
#         data = parser.parse_args()
#         # print(data['another'])
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)

#         else:
#             item.update(data)
#         return item


# class ItemList(Resource):
#     def get(self):
#         return{'items': items}


import sqlite3
from sqlite3.dbapi2 import Connection, connect
# from typing_extensions import Required
# from sqlite3.dbapi2 import Connection, Cursor
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, name):
      item = self.find_by_name(name)
      if item:
          return item
      return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        # return {'message': 'Item not found'}, 404

    def post(self, name):
        if self.find_by_name(name):
            return{'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['prise']}
       
        try:
            self.insert(item)

        except:
            return {"Message": "An error occurred inserting the item."},500
            
        return item, 201
    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data,db')
        cursor = connection.cursor()

        query ="INSERT INTO item VALUES (?,?)"
        cursor.execute(query,(item['name'],item['price']))

        connection.commit()
        connection.close()
        return item, 201

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query ="DELETE FROM item WHERE name=?"
        cursor.execute(query,(name,))

        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type=float,
                            required=True,
                            help='This field connot be left blank!'
                            )
        data = parser.parse_args()
        # print(data['another'])
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)

        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return{'items': items}
