#   The Pink Turnip
This blog aspires to be a community where users can exchange recipes, 
creating a library of vegetarian and vegan recipes to inspire people to 
start a more plant-based diet. 
It all starts one Monday at the time.

##  UX process
### Who is this site for?
This site targets people that are not necessarily vegetarian or vegan, 
but that are looking to start a more plant-based style.

### What does the user want to achieve in this site?
#####   Passive User:
*   This is a user that does not necessarily know the site and that is simply 
looking for inspiration.
-   As a user, I want to browse through recipes, so that I can find a recipe 
I want to make.
-   As a user, I want to be able to quickly identify if a recipe is vegan 
or vegetarian, so that I can make a my choice quickly.
-   As a user, I want to identify recipes that are quick to make, so that I 
can make a my choice quickly.
-   As a user, I want to be able to easily find the information I need in 
the recipe - ingredients, time it takes to prepare, and instructions.
-   As a user, I want to find brands and products that help me achieve a more 
plant-based diet and sustainable lifestyle.

#####   Active User:
*   This is a user that knows the site and wants to be part of the community 
and inspire others by sharing their own recipes.
-   As a user, I want to share recipes with others, so that others can replicate 
what I have made.
-   As a user, I want to see my name on the recipes, so that I can showcase 
my work.
-   As a user, I want to be able to edit and remove the recipes I have created.

### How can the user achieve this?
#####   Home page
- The user is able to browse through recipes by scrolling down the home page.
- If the user is logged in, a welcome message will be displayed.
- The user is able to navigate through the site by using the navigation menu.
- The user is able to easily see which category the recipes belong to as indicated by the 
category tag.
- The user is able to visalize approximately how long the recipe will take to make and 
how many people it will feed.

<div style="display: inline block;">
    <img width="400" height="300" src="/static/img/documentation/wireframe-home.png">
    <img width="400" height="300" src="/static/img/documentation/wireframe-home-2.png">
</div>

#####   Category
- The user is able to access individual categories through the navigation menu:
    - The user is able to choose between vegan or vegetarian recipes.
    - The user is able to access an additional category which is a filter selection for recipes 
    which duration is under 30 minutes.
    - The user is also able to access a page which collects all recipes.
    - The user is also able to log in to their profile.
- The user is able to visualize each individual recipe by clicking on the action 
hyperlink on each recipe card.
- The user is also able to access a 'Brands we love' category where they can see information 
about brands and possible sponsors that have meat or dairy replacement products.

<div style="display: inline block;">
    <img width="400" height="300" src="/static/img/documentation/wireframe-category.png">
</div>

#####   Single Recipe
- The user is able to visualize duration, portions, ingredients and instructions for each recipe.
- Once in the single recipe, the user is able to browse through other recipes by simply 
scrolling all the way down and clicking on another recipe.

#####   Profile Interactions
- The user is able to login by creating an account which requires a username and password.
- If the user is not logged in, the button displayed in navigator will say 'Login', if the 
user has already logged in the button will display 'Sign out'.
- The user is able to sign out of their account, which removes the cookie session by clicking on 
the Sign Out button.
- If the user is already logged in, the user will be redirected to his or her profile.
- Once the user has logged in, (s)he) is able to see the recipes (s)he has added to The Pink 
Turnip's library.
- The user is able to edit those recipes by clicking on the green edit button on the top left 
corner of each recipe.
- The user is also able to delete a recipe (s)he has created by simply clicking 
on the red button next to the edit button.
- The user is able to add a new recipe by clicking on the 'Add Recipe' button in their profile page.

<div style="display: inline block;">
    <img width="400" height="300" src="/static/img/documentation/wireframe-profile.png">
    <img width="400" height="300" src="/static/img/documentation/wireframe-add.png">
</div>

##  UX Features
This project's ideation started from the Assignment's Mandatory Requirements, and therefore the 
features will be explained in the same order, showing how the project fullfills these requirements.

###### Data handling:
- Created a MongoFB database connected to a Flask-based front-end.

###### Database structure:
- Created a database structure where recipes can be stored with all fields required for front and back-end.
- Created separate collections for Categories and Users which interact with the Recipes collection.
- Created a separate collection called Brands which does not interact with the other collections, it's purpose
it's to display information to front-end.

<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/data/collections.png">
    <img width="250" height="300" src="/static/img/documentation/data/collection-examples.png">
</div>
<div style="display: inline block;">
    <img width="600" height="300" src="/static/img/documentation/data/collections-interactions.png">
</div>

###### User functionality:
- Users are able to create, edit and delete records that they have added to the database.
- The user can access these records via their profile page.
- The user can interact with those records via the buttons available over each recipe in their profile page.
- In addition, the user is able to search the database by looking at different category pages.

###### Front-end:
- Created a navigation menu via templating in base.html that works both in desktop and mobile devices.
- Created Flask-based templates for the different pages needed for front-end, for example Recipe or Category pages.
- Used the Materialize library to speed up the design process.
- Used icons from both Materialize and Font Awesome libraries to make the interactions more intuitive.
- And added custom HTML and CSS to complete the options not available via the Materialize library.

###### Back-end:
- Imported all of the required libraries for this project.
- Connected the flask front-end to the MongoDB database under an env file which is ignored by git.
- Created a python file called app.py including all the routing needed such as rendering the templated html pages.
- Defined the data types that should be collected in the database when the user is adding or editing the documents 
contained.
- Created authentication requirements, where a user can not access certain pages unless a username is in session.

<div style="display: inline block;">
    <img width="300" height="300" src="/static/img/documentation/data/configuration.png">
    <img width="300" height="300" src="/static/img/documentation/data/routing.png">
</div>
<div style="display: inline block;">
    <img width="650" height="300" src="/static/img/documentation/data/data-types.png">
</div>

### Existing Features
###### Navigation:
- Fixed desktop navigation menu - the user is able to navigate through the site and access About, Categories, Brand, Profile and Sign In pages 
by using the navigation menu.
- Mobile navigation menu - when browsing from mobile devices, the user can access a side navigation menu that pops up when the user clicks on 
the burger icon on the top left.
- Sign In/Sign Out navigation - if a user is in session, the navigation button displays the 'Sign Out' option, if thtere is no username 
in session the option displayed is 'Sign In'. This is done via an if statement in the base.html file.

###### Viewing information:
- View existing records in the database - all users (without needing to log in) are able to view recipes that have been added to 
the database. This is done by using a for each statement in the jinja html template, so that each recipe is displayed.
- View single records from the database - this is done by using the routing in app.py to find one recipe from the collection via the 
Object(Id).
- View recipes by category - all users (without needing to log in) are able to see if recipes are vegan or vegetarian via the tag on 
each recipe preview card. This is done by using an if statement in the jinja html template.
- View recipes under 30 minutes - all users (without needing to log in) are able to view recipes which duration is under 30 minutes. 
This is not a user input, but rather a boolean data type set in app.py. When duration is under 30 minutes, the data field returns True, 
which allows us to display the filtered view of the recipes.
- View brands - all users (without needing to log in) are able to see the recommended brands. These are simply displayed from a 
separate collection called 'Brands'.
- View records created - once logged in, the user is able to see the records they have inputted under their profile page.

<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/home-page.png">
    <img width="250" height="300" src="/static/img/documentation/home-browse-page.png">
</div>
<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/categories/all-recipes-page.png">
    <img width="250" height="300" src="/static/img/documentation/categories/vegan-page.png">
    <img width="250" height="300" src="/static/img/documentation/recipes/single-page.png">
</div>
<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/about-page.png">
    <img width="250" height="300" src="/static/img/documentation/categories/brands-page.png">
</div>

###### Authentication of user:
- Register an account - to be able to interact with the database, the user must first create an account. The user is able to do so via the 
'Register an Account' template which adds a new record to the 'Users' collection.
- Sign In function - if the user tries to access the Profile Page, app.py checks if there is a username in session. If no username is in 
session the user is redirected to an html Sign In page.
- Sign Out function - if the user clicks on the Sign Out button at the top right corner of the navigation menu in desktop or bottom option 
in the mobile menu, the user is automatically logged out. The username in session is removed.

###### Interacting with the database:
- Create new records - once logged in, the user is able to submit new records to the database by filling in the 'Add Recipe' form. To 
do this we use the insert function in app.py combined with a jinja template form.
- Edit existing records - once logged in, the user is able to update the records (s)he has previously added by clicking on the 'Edit'
button over each recipe in their Profile Page. This is done by using the update function in app.py combined with a jinja template form.
- Delete existing records - once logged in, the user is able to remove records (s)he has previously added by clicking on the 'Edit'
button over each recipe in their Profile Page. This is done by using the remove function in app.py.

<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/profile/profile-page.png">
    <img width="250" height="300" src="/static/img/documentation/profile/add-recipe-page.png">
    <img width="250" height="300" src="/static/img/documentation/profile/edit-recipe-page.png">
</div>

###### Tracking:
- Google Analytics tracking pixel is installed, allowing to see traffic, users, devices, etc.

### Features Left to Implement
###### Viewing information:
- Search function to be able to find a recipe by keywords.
- New field in the database for type of meal ex. Breakfast, Snack, Lunch + as a new collection in the database.
- New field in the database for caloric content of each portion of the recipe.
- Display multiple images in each recipe as an option. If there are more pictures, they are displayed, if not then at least one image 
is required.

###### Interacting with the database:
- Adding the above new fields to the input forms.
- Upload file function as an alternative option to adding an already hosted image URL.

###### Authentication & Data Validation:
- Encypted password information using hash.
- Super Admin view where a new record needs to be 'approved' before it goes into live.

###### Data Protection:
- Adding T&C including GDPR clause and how the data is stored and for what purposes.

##  Languages
### Programming languages:
- HTML: Combined with Jinja, HTML is used to create the backbone and structure of the site.
  [Learn more about HTML.](https://www.w3schools.com/html/default.asp)
- CSS: Used to customize the visual outcome of the site, as well as to ensure via @media queries that the content displays nicely 
in all devices.
  [Learn more about CSS.](https://www.w3schools.com/css/default.asp)
- Javascript: Combined with JQuery, Javascript is used to deploy triggers that the user interacts with for example the input form 
and the navigation dropdown and side mobile menus.
  [Learn more about Javascript.](https://www.w3schools.com/js/default.asp)
- Python: Used to communicate with the database, routing and displaying html templates and manipulating data via the user interface.
  [Learn more about Python.](https://www.w3schools.com/python/default.asp)

### Libraries:
###### Structural:
- Flask: Used as a web framework, which combined with Jinja and Werkzeug are able to simplify the web development process and make a 
consistent framework.
  [Learn more about Flask.](https://flask.palletsprojects.com/en/1.1.x/)
- Jinja: Used as the templating engine to be able to create HTML pre-made layouts that can be then can be rendered via Python.
  [Learn more about Jinja.](https://jinja.palletsprojects.com/en/2.11.x/)
- Werkzeug: Used as the WSGI toolkit that Flask needs to run.
  [Learn more about Werkzeug.](https://palletsprojects.com/p/werkzeug/)

###### Styling and Interactions:
- JQuery: Used to be able to select elements in the HTML code based on their styling, and then modify them in Javascript. Often it 
has been part of Materialize components for this project.
  [Learn more about JQuery.](https://www.w3schools.com/jquery/jquery_intro.asp)
- Materialize: Used to speed up the development process by taking ready to use components and styling classes from the Materialize 
libarary for example cards which are used to display the recipes.
  [Learn more about Materialize.](https://materializecss.com/navbar.html)

### Tools:
###### Production Environment:
- Gitpod: Used as the coding environment for this project.
- Github: Used to store all repositories for this project, as well as to deploy the site via GitPages.

###### Tracking:
- Google Analytics: Used to track users behavior and traffic to the site.

###### Closing knowledge gaps:
- W3schools: Used to clarify and solidify knowledge acquired during the course.
- Stack Overflow: Used as support when troubleshooting and fixing bugs.


##  Testing
Manual tests have been conducted via the Google Chrome Developer Tools to verify that all pages are working properly. The site 
functionalities have been tested in live/deployed version by 3 other users from Android and iOs devices.

###### Navigation menu:
1. Desktop:
- The user is able to navigate to and from all pages via the navigation menu.
- In the desktop menu, the user is able to see the categories set in the dropdown menu.
- Sign In / Sign Out button in the navigator toggles according to whether the user is in session or not.

2. Mobile:
- The mobile menu triggers when the hamburger icon is clicked on.
- All of the options and icons in the menu display correctly.
- The navigation functionality has been checked in different devices incl. mobile devices via the Google Chrome Developer Tools.
- Sign In / Sign Out button in the navigator toggles according to whether the user is in session or not.

###### Home Page:
- The correct information displays from database records.
- All users (without needing to log in) are able to view recipes that have been added to the database.
- The correct tags display on each recipe card, either Vegan or Vegetarian.
- The contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.
- If a user is logged in, a welcome message displays, if a user is not logged in there is no message displaying.

###### Category Pages:
For all pages, the contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.

1. Vegan or Vegetarian template:
- The correct Category name is displayed from 'Category' collection.
- The correct Category description is displayed from 'Category' collection.
- The correct tags display on each recipe card, either Vegan or Vegetarian.
- The correct recipes show on each of the categories input by the user who created the recipe, either Vegan or Vegetarian.

2. Express template:
- The correct recipes display under the Express Page, since all of the recipes are under 30 minutes duration.

3. Brands template:
- All of the required fields of each of the items in 'Brands' collection display properly (title, category, imageURL, description, key 
bullet points).

###### Profile Page:
For all pages, the contents resize and are able to be seen properly in all different devices. This function has been testsed by using Google 
Chrome Developer Tools.
- The user is able to see the records (s)he has added to the database.
- If the user has not previously added a record, a message is displayed.
- Each record displays a 'Edit' and 'Delete' icons on the top left corner.
- These icons redirect properly and start the function called.

1. Add a record:
- The Add Recipe form and all of the fields display correctly.
- The Submit button works properly and adds a new record to the database.

2. Edit a record:
- The Edit Recipe form and all of the fields display correctly displaying the records in key fields previously input in the database.
- The Submit button works properly and the record is updated.

3. Delete a record:
- The record selected is deleted from the database.

###### Authentication & User Pages:
- If there is no username in session, the user is prompt to a Sign In form.
- If the user does not have an account, the Register link under the Sign In form works properly.
- A user that is not sign in can not access the Profile Page view.

1. Register:
- The user is able to create an account by interacting with the registration form.

2. Sign In:
- The user is able to log in by inputting a registered username and password to the Sign In form.
- If the password or username is not correct, the same form is reloaded empty.

3. Sign Out:
- When the user clicks on the Sign Out button, the user is automatically logged out.
- The session username is removed from the cookie which we can see in Google Chrome Developer Tools.


## Deployment
This application is hosted in Heroku, which you would need an account for.
###### To deploy this project yourself:
1. Copy the repository from Github.
2. Open a Heroku account.
3. Create a new project under Heroku.
4. Go to the Settings tab in Heroku.
5. Scroll down and click on Config Var to reveal the Config Variables.
    Here we need to add the following variables:
    - IP - which IP you can access this app from.
    - MONGO_URI - which allows you to connect to the MongoDB database.
    - PORT - which is set by default by Heroku.
    - SECRET KEY 
5. Go to the Deploy tab in Heroku.
6. Connect Heroku to Github directly via API connector.
7. When propted, logged in to your Github account. If everything went well, the Github sub-tab should say Connected in green.
8. In the same tab, make sure that the right repository is connected.
9. Select automatic deployments to Master to make the updating of the site easier.


## Credits
###### Content
- Placeholder Loreipsum text has been placed in some pages.

###### Media:
- Unsplash: Used to get all the stock photo material. This is a library where amateur photographers around the world upload their 
pictures and make them available to other users for free.
  [Learn more about Canva.](https://unsplash.com/s/photos/vegetarian)
- Canva Online Editor: Used to do any graphic design used on this site such as resizing pictures or creating the logo.
  [Learn more about Canva.](https://www.canva.com/)
- Font Awesome: Used to get icons making it a more intuitive experience for the user such as for example having a User icon leading 
to the Profile page.
  [Learn more about Font Awesome.](https://fontawesome.com/icons?d=gallery)

###### Login System:
- Julian Nash's tutorials have been fundamental to closing some of the knowledge gaps that I had starting 
this project. I was able to work with session cookies in Flask.
    [See the tutorial here - 'The Flask session object', YouTube tutorial.](https://www.youtube.com/watch?v=PYILMiGxpAU)
    [See the tutorial here - 'The Flask session object', Web tutorial.](https://pythonise.com/series/learning-flask/flask-session-object)
- I have also benefited from other tutorials to reinforce my knowledge such as the one provided in the YouTube channel Pretty Printed 
and Tech with Tim.
    [See the tutorial here - Pretty Printed tutorial.](https://www.youtube.com/watch?v=vVx1737auSE)
    [See the tutorial here - Tech with Tim tutorial.](https://www.youtube.com/watch?v=iIhAfX4iek0&t=432s)

###### Documentation:
At the start of this project, I reviewed some of my classmates submitted milestone III projects which were submitted in the Slack channel 
for peer reviews. One which I found via LinkedIn really impressed me especially due to the attention to detail and overall effort put into 
the documentation and commit logs. It inspired me to also add images and style my documentation and commit messages.
    [See the project - Home Chopped.](https://github.com/Frozenaught/homechopped/tree/master/app)

## Acknowledgements
Many thanks to my mentor Moosa for encouraging me to continue in this program, and to the Code Institute staff who kindly adapted my 
schedule and gave me a few extra weeks.

And thank you to my fiancé, Jonatan, for his patience and kindness and for being a true partner taking care of us so that I could time 
to work on my school assignments.

And to my brain and body for coping with a full-time job and a challenging program, both highly demanding especially 
in these past months, but both equally rewarding.