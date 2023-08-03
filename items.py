from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3 

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank!")
    @jwt_required()
    def get(self, name):
       connection = sqlite3.connect('data.db')
       cursor = connection.cursor()

       query =  "SELECT * FROM items WHERE name=?"
       result = cursor.execute(query, (name,))

       row = result.fetchone()
       connection.close()

       if row:
            return {"item" : {"name" : row[0],"price" : row[1]}}
       return {"message" : "Item not found"}, 404

    def post(self, name):
        data = request.get_json(silent = True)
        item = {"name" : name, "price" : 12.33}
        items.append(item)
        return item , 201
    
    def delete(self, name):
        connection = sqlite3.Connection('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return "Item deleted"




class ItemList(Resource):
    def get(self):
        return {"items" : items}
