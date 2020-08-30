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


![Home Page](/static/img/documentation/home-page.png)
![alt text](https://github.com/a-telier/blog/static/img/documentation/home-browse-page.png)

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

![alt text](https://github.com/a-telier/blog/static/img/documentation/categories/all-recipes-page.png)
![alt text](https://github.com/a-telier/blog/static/img/documentation/categories/vegan-page.png)
![alt text](https://github.com/a-telier/blog/static/img/documentation/categories/brand-page.png)

#####   Single Recipe
- The user is able to visualize duration, portions, ingredients and instructions for each recipe.
- Once in the single recipe, the user is able to browse through other recipes by simply 
scrolling all the way down and clicking on another recipe.

![alt text](https://github.com/a-telier/blog/static/img/documentation/recipes/single-page.png)
![alt text](https://github.com/a-telier/blog/static/img/documentation/recipes/single-page-others.png)


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

![alt text](https://github.com/a-telier/blog/static/img/documentation/profile/profile-page.png)
![alt text](https://github.com/a-telier/blog/static/img/documentation/profile/add-recipe-page.png)
![alt text](https://github.com/a-telier/blog/static/img/documentation/profile/edit-recipe-page.png)


Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features Left to Implement
Another feature idea
Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

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