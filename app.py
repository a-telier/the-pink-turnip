import os

#   full stack framework for template development
from flask import Flask, render_template, redirect, request, url_for

#   libraries to interact with database Mongo DB
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

#   this code imports env
#   where passwords are stored for ex
#   but not deployed to public
from os import path
# import env as config


#   start an instance of Flask
app = Flask(__name__)

#   file is only pulled when working on your code in your workspace
if path.exists("env.py"):
    import env

# configuration of Database
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')

#   create an instance of PyMongo
mongo = PyMongo(app)


@app.route('/')
def get_editorials():
    return render_template("home.html", editorials=mongo.db.editorials.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

