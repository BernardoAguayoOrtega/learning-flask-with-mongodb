from flask import Flask, Response
from flask_pymongo import PyMongo
from flask import request
from werkzeug.security import generate_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://dbAdmin:dbAdmin.@cluster0.zugnm.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def welcome():
  return 'welcome'

@app.route('/users', methods=['GET'])
def get_users():

    users = mongo.db.users.find()
    response = json_util.dumps(users)

    return Response(response, mimetype='application/json'), 200

@app.route('/users', methods=['POST'])
def create_user():

    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and email and password:

        hashed_password = generate_password_hash(password)

        id = mongo.db.users.insert({
            'username': username,
            'email': email,
            'password': hashed_password
        })

        response = {
            'id': str(id),
            'username': username,
            'email': email,
            'password': hashed_password
        }

        return response

    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + str(request.url),
        'status': 404
    }

    return message, 404


@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):

    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    
    response = json_util.dumps(user)

    return Response(response, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)

# dbAdmin
# dbAdmin.
# mongodb+srv://dbAdmin:dbAdmin.@cluster0.zugnm.mongodb.net/database?retryWrites=true&w=majority