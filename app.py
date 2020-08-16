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


#############################################
#    AUTHENTICATION
#############################################

#   REFERENCE CREDITS:
#   Login System ->
#   https://www.youtube.com/watch?v=vVx1737auSE, https://www.youtube.com/watch?v=PYILMiGxpAU
#   https://pythonise.com/series/learning-flask/flask-session-object
#   Sessions in Flask ->
#   https://www.youtube.com/watch?v=iIhAfX4iek0&t=432s

#   SIGNIN TO YOUR ACCOUNT
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        session['username'] = request.form['username']
        print("This is your session username " + session["username"])

        if session['username'] in session:
            print("This user is already in session")
            return redirect(url_for("profile"))
        else:
            return redirect(url_for("login"))

        if session['username'] not in session:
            users = mongo.db.users.find()
            username = request.form.get("username")
            password = request.form.get("password")

            if username in users and password in users:
                print("This user exists in our database, you will be redirected to your profile!")
                return redirect(url_for("profile"))
            else:
                print("Sorry, we can't compute. Please login to your profile.")
                return redirect(url_for("login"))
        else:
            return redirect(request.url)

            
    return render_template("users/login.html")

#   REGISTER A NEW USER


@app.route('/new_user', methods=['GET'])
def new_user():
    return render_template("users/register.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    # return render_template("users/register.html")
    username = request.form.get("username")
    password = request.form.get("password")
    user = mongo.db.users.find({"username": username})

    new_user = {
        "username": username,
        "password": password,
    }

    #   checks if the usernmae input is already in db
    #   user does not exist in database
    if user is not None:
        mongo.db.users.insert_one(new_user)
        print("New user registered, welcome!")
        return redirect(url_for("get_vege"))
    else:
        #   user already exists in the database
        #   please login to your account
        print("The user already exists, please choose another username")
        return redirect(url_for("get_vegan"))

#   YOUR PROFILE
@app.route('/profile', methods=['GET'])
def profile():

    user = session["username"]

    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        return render_template("users/profile.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("login"))


###########################################
#    GENERAL/DISPLAY PAGES
###########################################

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


#############################################
#    INTERACT WITH DATABASE
#############################################

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
