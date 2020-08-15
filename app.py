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

##########################
#    GENERAL/DISPLAY PAGES
##########################

@app.route('/')
@app.route('/home')
def get_recipe():
    if 'username' in session:
        return render_template("home.html", recipes=mongo.db.recipes.find(), message='You are logged in as ' + session['username'])

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

############################
#    AUTHENTICATION
############################

# REFERENCE CREDITS:
# Login System ->
# https://www.youtube.com/watch?v=vVx1737auSE, https://www.youtube.com/watch?v=PYILMiGxpAU

#   PROFILE
@app.route('/profile')
def profile():

    #   if there is an active session:
    if session.get('USERNAME', None) is not None:
        #   get information from db.users
        username = session.get('USERNAME')
        return render_template('profile.html', user=mongo.db.users.find_one())
    else:
        print("User not in session")
        return render_template('signin.html')

#   SIGNIN
@app.route('/signin', methods=['GET', 'POST'])
def signin():

    users = mongo.db.users

    if request.method == 'POST':
        #   checks if the input matches something in db
        username = users.find_one({'username': request.form.get('username')})
        password = users.find_one({'password': request.form.get('password')})

        #   if the input username is different than those in users db
        #   1) This username is not in db
        if username != users:
            print('Username not found!')
            return redirect(request.url)
        
        #   2) This username is not already in db
        #   we will accept the new username
        else:
            login_user = username

        if not password == login_user['password']:
            print('Password incorrect')
            return redirect(request.url)

        else:
            #   assign session value to username
            session['USERNAME'] = user['username']
            print('User has been added to session')

            return redirect(url_for('profile'))

    return render_template('signin.html')




    # if login_user:
    #     if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']).encode('utf-8') == login_user['password'].encode('utf-8'):
    #         session['username'] = request.form['username']
    #         return redirect(url_for('profile'))
    
    # return 'Invalid username or password'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        registered_users = users.find_one({'name': request.form['username']})
        
        # if there is no registered user
        if registered_users is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # add the new user to the database
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            # now session username is the same as in the request form
            session['username'] = request.form['username']
            # redirect to the profile page
            return redirect(url_for('profile'))

        elif registered_users is not None:
            return redirect(url_for('profile'))

        # return 'That username already exists'

    return render_template('register.html')

############################
#    INTERACT WITH DATABASE
############################

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
