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
import datetime

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
#    GENERAL PAGES
#############################################

#   HOME
@app.route('/')
@app.route('/home')
def get_recipe():
    if 'username' in session:
        return render_template("home.html", recipes=mongo.db.recipes.find(),
        message='Welcome, you are logged in as ' + session['username'])

    return render_template("home.html",
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find())

#   ABOUT
@app.route('/about')
def about():
    return render_template("about.html")

#   BRANDS WE LOVE
@app.route('/brands')
def brands():
    return render_template("brands.html", brands=mongo.db.brands.find())


#############################################
#    USER INTERACTIONS
#############################################

#   REFERENCE CREDITS:
#   Login System ->
#   https://www.youtube.com/watch?v=vVx1737auSE
#   https://www.youtube.com/watch?v=PYILMiGxpAU
#   https://pythonise.com/series/learning-flask/flask-session-object
#   Sessions in Flask ->
#   https://www.youtube.com/watch?v=iIhAfX4iek0&t=432s

#   SIGN IN TO YOUR ACCOUNT
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        #   the user is already logged in
        if "username" in session:
            print("You are already sign in, welcome " + session["username"])
            return redirect(url_for("profile"))

    #   if user is entering login information
    if request.method == "POST":
        #   creates a new object
        current_user = {
            "username": request.form.get("username"),
            "password": request.form.get("password"),
        }
        #   looks for username with current inputted username
        user = mongo.db.users.find_one({"username": current_user["username"]})

        #   check if the username exists in db
        #   if user exists:
        if user is not None:
            #   we will check if the password matches our record
            #   password matches
            if current_user["password"] == user["password"]:
                print("You have entered the correct password, and will go to profile")
                #   assign username entered to current session
                session['username'] = request.form['username']
                return redirect(url_for("profile"))
            #   password does not match
            else:
                print("You have entered the wrong password, try again.")
                return redirect(request.url)

        #   user does not exist:
        else:
            print("We could not find your username, please register first.")
            return redirect(url_for("register"))

    else:
        return render_template("users/login.html")

#   LOG OUT OF YOUR ACCOUNT
@app.route("/sign-out")
def sign_out():
    session.pop("username", None)
    print("User has been sign out")
    return redirect(url_for("login"))

#   REGISTER A NEW USER
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
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
            return redirect(url_for("profile"))
        else:
            #   user already exists in the database
            print("The user already exists, please choose another username")
            return redirect(url_for("register"))

    else:
        #   the method is GET, therefore do:
        return render_template("users/register.html")

#   DISPLAY YOUR PROFILE
@app.route('/profile', methods=['GET'])
def profile():
    if "username" in session:
        print("User is logged in, display the profile page of user.")
        current_user = {
            "username": session["username"],
        }
        #   looks for username with current inputted username
        user = mongo.db.recipes.find_one({"username": current_user["username"]})

        return render_template("users/profile.html",
            recipes=mongo.db.recipes.find())

    else:
        print("You need to login to access your profile page.")
        return redirect(url_for("login"))


#############################################
#    RECIPE INTERACTIONS
#############################################

#   ADD A NEW RECIPE
@app.route('/add_recipe')
def add_recipe():
    if "username" in session:
        print("User is logged in, display the profile page of user.")
        return render_template("recipe/addrecipe.html",
        recipes=mongo.db.recipes.find(),
        categories=mongo.db.categories.find())
    else:
        print("You need to login to access your profile page.")
        return redirect(url_for("login"))

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():

    #  if a recipe can be made in 30m or less
    if int(request.form.get('duration')) <= 30:
        isUnder30 = True
    else:
        isUnder30 = False

    recipeDict = {
        "date": datetime.datetime.now(),  # returns the date for today
        "name": request.form.get('name'),
        "imageURL": request.form.get('imageURL'),
        "ingredients": str(request.form.get('ingredients')).split(sep=", "),
        "instructions": str(request.form.get('instructions')).split(sep=", "),
        "duration": int(request.form.get('duration')),
        "portions": int(request.form.get('portions')),
        "isVegan": bool(request.form.get('isVegan')),
        "isVegetarian": bool(request.form.get('isVegetarian')),
        "isUnder30": bool(isUnder30),
        "username": session["username"],
    }

    recipe = mongo.db.recipes
    recipe.insert_one(recipeDict)
    return redirect(url_for('get_recipe'))


#   EDIT AN EXISTING RECIPE
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    if "username" in session:
        print("User is logged in, and can edit his/her recipes.")
        recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template('recipe/editrecipe.html', recipe=recipe)
    else:
        print("You need to login to access your profile page.")
        return redirect(url_for("login"))

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):

    #  if a recipe can be made in 30m or less
    if int(request.form.get('duration')) <= 30:
        isUnder30 = True
    else:
        isUnder30 = False

    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        "date": datetime.datetime.now(),  # returns the date for today
        "name": request.form.get('name'),
        "imageURL": request.form.get('imageURL'),
        "ingredients": str(request.form.get('ingredients')).split(sep=", "),
        "instructions": str(request.form.get('instructions')).split(sep=", "),
        "duration": int(request.form.get('duration')),
        "portions": int(request.form.get('portions')),
        "isVegan": bool(request.form.get('isVegan')),
        "isVegetarian": bool(request.form.get('isVegetarian')),
        "isUnder30": bool(isUnder30),
        "username": session["username"],
    })
    return redirect(url_for('get_recipe'))

#   DELETE RECIPES
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('profile'))

#   SHOW RECIPES
@app.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    # The web framework gets post_id from the URL and passes it as a string
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # displays each individual recipe's information
    # fetches the data based on the _id
    return render_template("recipe/recipe.html",
    recipes=mongo.db.recipes.find(),
    recipe=recipe)


###########################################
#    CATEGORIES
###########################################

@app.route('/vegetarian')
def get_vege():
    return render_template("category/vegetarian.html",
    recipes=mongo.db.recipes.find())
    return redirect(url_for('show_recipe'))

@app.route('/vegan')
def get_vegan():
    return render_template("category/vegan.html",
    recipes=mongo.db.recipes.find())
    return redirect(url_for('show_recipe'))

@app.route('/express')
def get_express():
    return render_template("category/express.html",
    recipes=mongo.db.recipes.find())
    return redirect(url_for('show_recipe'))

@app.route('/allrecipes')
def all_recipes():
    return render_template("category/allrecipes.html", recipes=mongo.db.recipes.find())

###########################################
#    ERROR HANDLING
###########################################
#   REFERENCE CREDITS:
#   https://flask.palletsprojects.com/en/1.1.x/errorhandling/


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
