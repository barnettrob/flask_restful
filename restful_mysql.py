# RESTful API creation using Flask.
# Based off of the below tutorial but with changes to use MySQL
# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# For MySQL changes, see https://codehandbook.org/python-web-application-flask-mysql/
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flaskext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()

# MySQL configurations.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Make MYSQL init call with app.
mysql.init_app(app)

class User(Resource):
    def get(self, name):
        # MySQL connection.
        conn = mysql.connect()
        cursor = conn.cursor()
        user_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(user_query, (name,))
        user = cursor.fetchone()
        if user:
            return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age");
        parser.add_argument("occupation")
        args = parser.parse_args()

        # MySQL connection.
        conn = mysql.connect()
        cursor = conn.cursor()
        user_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(user_query, (name,))
        exists = cursor.fetchone()
        if exists:
            return "User with name {} already exists".format(name), 400
        else:
            # Insert.
            insert_query = ("INSERT INTO user (name, age, occupation) VALUES (%s, %s, %s)")
            cursor.execute(insert_query, (name, int(args["age"]), args["occupation"],))
            conn.commit()

        user_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(user_query, (name,))
        user = cursor.fetchone()
        if user:
            return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()


        # MySQL connection.
        conn = mysql.connect()
        cursor = conn.cursor()
        user_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(user_query, (name,))
        exists = cursor.fetchone()
        if not exists:
            return "User with name {} does ot exist".format(name), 400
        else:
            update_query = ("UPDATE user SET age = %s, occupation = %s WHERE name = %s")
            cursor.execute(update_query, (int(args["age"]), args["occupation"], name,))
            conn.commit()

        user_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(user_query, (name,))
        user = cursor.fetchone()
        if user:
            return user, 200

    def delete(self, name):
        # MySQL connection.
        conn = mysql.connect()
        cursor = conn.cursor()
        user_query = "SELECT * FROM user WHERE name = %s"
        cursor.execute(user_query, (name,))
        exists = cursor.fetchone()
        if not exists:
            return "User with name {} does ot exist".format(name), 400
        else:
            delete_query = ("DELETE FROM user WHERE name = %s")
            cursor.execute(delete_query, (name,))
            conn.commit()

        return "{} is deleted.".format(name), 200

class List(Resource):
    def get(self):
        # MySQL connection.
        conn = mysql.connect()
        cursor = conn.cursor()
        users_query = "SELECT * FROM user"
        cursor.execute(users_query)
        users = cursor.fetchall()
        return users, 200

api.add_resource(User, "/user/<string:name>")
api.add_resource(List, "/users/list")
app.run(debug=True)