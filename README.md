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
    <img width="250" height="300" src="/static/img/documentation/home-page.png">
    <img width="250" height="300" src="/static/img/documentation/home-browse-page.png">
    <img width="250" height="300" src="/static/img/documentation/about-page.png">
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
    <img width="250" height="300" src="/static/img/documentation/categories/all-recipes-page.png">
    <img width="250" height="300" src="/static/img/documentation/categories/vegan-page.png">
    <img width="250" height="300" src="/static/img/documentation/categories/brands-page.png">
</div>

#####   Single Recipe
- The user is able to visualize duration, portions, ingredients and instructions for each recipe.
- Once in the single recipe, the user is able to browse through other recipes by simply 
scrolling all the way down and clicking on another recipe.

<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/recipes/single-page.png">
    <img width="250" height="300" src="/static/img/documentation/recipes/single-page-others.png">
</div>

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
    <img width="250" height="300" src="/static/img/documentation/profile/profile-page.png">
    <img width="250" height="300" src="/static/img/documentation/profile/add-recipe-page.png">
    <img width="250" height="300" src="/static/img/documentation/profile/edit-recipe-page.png">
</div>

##  UX Features
This project's ideation started from the Assignment's Mandatory Requirements, and therefore the 
features will be explained in the same order, showing how the project fullfills these requirements.

##### Data handling:
- Created a MongoFB database connected to a Flask-based front-end.

##### Database structure:
- Created a database structure where recipes can be stored with all fields required for front and back-end.
- Created separate collections for Categories and Users which interact with the Recipes collection.
- Created a separate collection called Brands which does not interact with the other collections, it's purpose
it's to display information to front-end.

<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/data/collection-example.png">
    <img width="250" height="300" src="/static/img/documentation/data/collections.png">
</div>
<div style="display: inline block;">
    <img width="250" height="600" src="/static/img/documentation/data/collections-interactions.png">
</div>

##### User functionality:
- Users are able to create, edit and delete records that they have added to the database.
- The user can access these records via their profile page.
- The user can interact with those records via the buttons available over each recipe in their profile page.
- In addition, the user is able to search the database by looking at different category pages.

##### Front-end:
- Created a navigation menu via templating in base.html that works both in desktop and mobile devices.
- Created Flask-based templates for the different pages needed for front-end, for example Recipe or Category pages.
- Used the Materialize library to speed up the design process.
- Used icons from both Materialize and Font Awesome libraries to make the interactions more intuitive.
- And added custom HTML and CSS to complete the options not available via the Materialize library.

##### Back-end:
- Imported all of the required libraries for this project.
- Connected the flask front-end to the MongoDB database under an env file which is ignored by git.
- Created a python file called app.py including all the routing needed such as rendering the templated html pages.
- Defined the data types that should be collected in the database when the user is adding or editing the documents 
contained.
- Created authentication requirements, where a user can not access certain pages unless a username is in session.

<div style="display: inline block;">
    <img width="250" height="300" src="/static/img/documentation/data/configuration.png">
    <img width="250" height="300" src="/static/img/documentation/data/routing.png">
</div>
<div style="display: inline block;">
    <img width="600" height="300" src="/static/img/documentation/data/data-types.png">
</div>

### Existing Features
###### Viewing information in a visually appealing way:
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

###### Authentication of user:
- Register an account - to be able to interact with the database, the user must first create an account. The user is able to do so via the 
'Register an Account' template which adds a new record to the 'Users' collection.
- Sign In function - if the user tries to access the Profile Page, app.py checks if there is a username in session. If no username is in 
session the user is redirected to an html Sign In page.
- Sign Out function - if the user clicks on the Sign Out button at the top right corner of the navigation menu in desktop or bottom option 
in the mobile menu, the user is automatically logged out. The username in session is removed.
- Sign In/Sign Out navigation - if a user is in session, the navigation button displays the 'Sign Out' option, if thtere is no username 
in session the option displayed is 'Sign In'. This is done via an if statement in the base.html file.

###### Interacting with the database:
- Create new records - once logged in, the user is able to submit new records to the database by filling in the 'Add Recipe' form. To 
do this we use the insert function in app.py combined with a jinja template form.
- Edit existing records - once logged in, the user is able to update the records (s)he has previously added by clicking on the 'Edit'
button over each recipe in their Profile Page. This is done by using the update function in app.py combined with a jinja template form.
- Delete existing records - once logged in, the user is able to remove records (s)he has previously added by clicking on the 'Edit'
button over each recipe in their Profile Page. This is done by using the remove function in app.py.


Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
Features Left to Implement
Another feature idea

=============

Languages

- HTML: Used to create the backbone and structure of the site.
- CSS: Used to customize the visual outcome of the site. As well as to ensure via @media queries that the content displays nicely in all devices.
- Javascript: Used to define the game mechanics, navigation as well as the interactions with the different html and DOM elements.
Libraries
- JQuery: Used to be able to select elements in the HTML code based on their styling, and then modify them in Javascript.
- Python:

Other tools
Templating
- Jinja
- Flask

Styling
- Materialize
- Font Awesome
- Canva Online Editor: Used to edit all of the graphic material used on this site.

Production
- Gitpod: Used as the coding environment for this project.
- Github: Used to store all repositories for this project, as well as to deploy the site via GitPages.

Tracking
- Google Analytics: Used to track users behavior and traffic to the site.

Others
- W3schools: Used to clarify and solidify knowledge acquired during the course.
- Stack Overflow: Used as support when troubleshooting and fixing bugs.


5. Structure: Incorporate a main navigation menu and structured layout (you might want to use Materialize or Bootstrap to accomplish this).
6. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
7. Version control: Use Git & GitHub for version control.
8. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
9. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
10. Make sure to not include any passwords or secret keys in the project repository.

=============

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X




CREDITS
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet