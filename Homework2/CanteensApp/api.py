from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)


class CanteenResource(Resource):
    def get(self, id=None, time_open=None):

        # Connect to the SQLite database
        conn = sqlite3.connect('database/DINERS.db')
        c = conn.cursor()

        if id:
            # Retrieve a specific canteen
            c.execute("SELECT * FROM CANTEEN WHERE ID = ?;", (id,))
            canteens = c.fetchall()
        elif time_open:
            # Retrieve canteens by open time
            c.execute("SELECT * FROM CANTEEN WHERE time_open = ?;", (time_open,))
            canteens = c.fetchall()
        else:
            # Retrieve all canteens
            c.execute("SELECT * FROM CANTEEN;")
            canteens = c.fetchall()

        # Close the connection
        conn.close()

        return canteens

    def post(self):

        # Connect to the SQLite database
        conn = sqlite3.connect('database/DINERS.db')
        c = conn.cursor()

        # Get the data from the request
        data = request.get_json()

        # Insert the new canteen into the database
        c.execute("INSERT INTO CANTEEN (Name, Location, time_open, time_closed) VALUES (?, ?, ?, ?);",
                  (data['Name'], data['Location'], data['time_open'], data['time_closed']))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return {'message': 'New canteen added'}

    def put(self, id):

        # Connect to the SQLite database
        conn = sqlite3.connect('database/DINERS.db')
        c = conn.cursor()

        # Get the data from the request
        data = request.get_json()

        # Update the canteen in the database
        c.execute("UPDATE CANTEEN SET Name = ?, Location = ?, time_open = ?, time_closed = ? WHERE ID = ?;",
                  (data['Name'], data['Location'], data['time_open'], data['time_closed'], id))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return {'message': 'Canteen updated'}

    def delete(self, id):

        # Connect to the SQLite database
        conn = sqlite3.connect('database/DINERS.db')
        c = conn.cursor()

        # Delete the canteen from the database
        c.execute("DELETE FROM CANTEEN WHERE ID = ?;", (id,))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return {'message': 'Canteen deleted'}


api.add_resource(CanteenResource, '/canteen', '/canteen/<int:id>', '/canteen/<string:time_open>')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port=5001, debug=True)
