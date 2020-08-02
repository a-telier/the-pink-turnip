import os

#   full stack framework for template development
from flask import Flask, render_template, redirect, request, url_for

#   libraries to interact with database Mongo DB
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

#   this code imports env where passwords are stored for ex but not public
from os import path

#   used in datepicker
import datetime

today = datetime.datetime.now()


#   start an instance of Flask
app = Flask(__name__)

#   file is only pulled when working on your code in your workspace
#   import env as config, also works
if path.exists("env.py"):
    import env

# configuration of Database
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')

#   create an instance of PyMongo
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("home.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", recipes=mongo.db.recipes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():

    recipeDict = {
        "date": request.form.get('dateAdded'),
        "name": request.form.get('name'),
        "imageURL": request.form.get('imageURL'),
        "ingredients": request.form.get('ingredients'),
        "instructions": request.form.get('instructions'),
        "duration": int(request.form.get('duration')),
        "portions": int(request.form.get('portions')),
        "isVegan": bool(request.form.get('isVegan')),
        "isVegetarian": bool(request.form.get('isVegetarian')),
    }

    recipe = mongo.db.recipes
    recipe.insert_one(recipeDict)
    return redirect(url_for('get_recipe'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)