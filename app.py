from flask import Flask,make_response
from flask_migrate import Migrate
from models import db,User


# create flask application object
app = Flask(__name__)

#configure a database connection to the local file app.db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

#disable modification tracking to use less memory


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

#create a migrate object  to manage schema modification

migrate = Migrate(app, db)

#initialize the flask application to use the database
db.init_app(app)

@app.route('/')

def index():
    return  "Welcome to flask"

@app.route('/users/<username>')
def get_username(username):
    return f"Hello, {username}"

@app.route("/users")
def get_users():
    users = [{"id": User.id,"username":User.username,"age":User.age } for User in User.query.all()]
    # print(users)
    # return users
    # response = make_response(jsonify([user.to_dict() for user in users]), 200)
    return make_response (users,200)

if  __name__ == '__main__':
    app.run(port= 5500 , debug= True)