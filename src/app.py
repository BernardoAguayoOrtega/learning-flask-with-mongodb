from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI']='mongodb+srv://dbAdmin:dbAdmin.@cluster0.zugnm.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/users')
def create_user():
  return {'message': 'received'}

if __name__ == '__main__':
  app.run(debug=True)

#dbAdmin
#dbAdmin.
#mongodb+srv://dbAdmin:dbAdmin.@cluster0.zugnm.mongodb.net/database?retryWrites=true&w=majority
