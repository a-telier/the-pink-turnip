import os
# import pandas as pd
# import numpy as np

#   full stack framework for template development
from flask import Flask, render_template, redirect, request, url_for, session

#   libraries to interact with database Mongo DB
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

#   this code imports env where passwords are stored for ex but not public
from os import path
#   to make it more difficult to decrypt passwords
import bcrypt

#   used in datepicker
#   import datetime

#   start an instance of Flask
app = Flask(__name__)

#   file is only pulled when working on your code in your workspace
#   import env as config, also works
if path.exists("env.py"):
    import env

#   configuration of Database
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#   create an instance of PyMongo
mongo = PyMongo(app)


# GENERAL
@app.route('/')
@app.route('/home')
def get_recipe():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template("home.html", recipes=mongo.db.recipes.find())

@app.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    # The web framework gets post_id from the URL and passes it as a string
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # displays each individual recipe's information
    # fetches the data based on the _id
    return render_template("recipe.html",
    recipes=mongo.db.recipes.find_one(),
    recipe=recipe)

# BY CATEGORY
@app.route('/vegetarian')
def get_vege():
    return render_template("vegetarian.html", recipes=mongo.db.recipes.find())
    return redirect(url_for('show_recipe'))

@app.route('/vegan')
def get_vegan():
    return render_template("vegan.html", recipes=mongo.db.recipes.find())

@app.route('/express')
def get_express():
    return render_template("express.html", recipes=mongo.db.recipes.find())


#   USER INTERACTIONS
#   LOGIN
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']).encode('utf-8') == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    
    return 'Invalid username or password'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        registered_users = users.find_one({'name': request.form['username']})
        
        if registered_users is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('/login'))

        return 'That username already exists'

    return render_template('register.html')

#   INSERT USER INPUT
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", recipes=mongo.db.recipes.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():

    #  if a recipe can be made in 30m or less
    if int(request.form.get('duration')) <= 30:
        isUnder30 = True
    else:
        isUnder30 = False

    recipeDict = {
        "date": datetime.datetime.utcnow(),  # returns the date for today
        "name": request.form.get('name'),
        "imageURL": request.form.get('imageURL'),
        "ingredients": str(request.form.get('ingredients')).split(sep=", "),
        "instructions": str(request.form.get('instructions')).split(sep=", "),
        "duration": int(request.form.get('duration')),
        "portions": int(request.form.get('portions')),
        "isVegan": bool(request.form.get('isVegan')),
        "isVegetarian": bool(request.form.get('isVegetarian')),
        "isUnder30": bool(isUnder30),
    }

    recipe = mongo.db.recipes
    recipe.insert_one(recipeDict)
    return redirect(url_for('get_recipe'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
