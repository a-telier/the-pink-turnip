import os

#   full stack framework for template development
from flask import Flask, render_template, redirect, request, url_for

#   libraries to interact with database Mongo DB
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#   this code imports env
#   where passwords are stored for ex
#   but not deployed to public
from os import path
#   file is only pulled when working on your code in your workspace
if path.exists("env.py"):
    import env 
#   get secret key
SECRET_KEY = os.environ.get('SECRET_KEY') 


#   start an instance of Flask
app = Flask(__name__)

#   connect to 'blog' Mongo DB database
app.config["MONGO_DBNAME"] = 'blog'
app.config["MONGO_URI"] = "mongodb+srv://alex-rabi:Domenica16@blog.wvugx.mongodb.net/blog?retryWrites=true&w=majority"

#   create an instance of PyMongo
mongo = PyMongo(app)



@app.route('/')
@app.route('/get_tasks')


def get_tasks():
    return render_template("blog.html", blog=mongo.db.blog.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)