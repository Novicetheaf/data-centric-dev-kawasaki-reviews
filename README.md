# **Data Centric Development Kawasaki Reviews**

This is my Kawasaki motorcycle review site, which gives the end-user an array  of models that have critic reviews that can be viewed for interested users. It also has the option for user to add their own reviews, edit a review and delete a review.  

The idea for this site is to show CRUD functionality with python and mongodb. The site uses a modal form to add a user review, which is placed in the navbar for quick access.

In the critic reviews section the user can see all the models that have been reviewed by critics, and they get a snapshot of what each bike is like. They can click the 'see more' option below each review and this will filter that specific motorcycle by the id of the model and give them a more in depth review.

The web app also contains forms of contacting me in my footer, via conact me modal, github and linkedin.
 
 
## Demo

A live demo can be viewed [here](https://data-centric-dev-bike-reviews.herokuapp.com/ )

![Desktop Demo](https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/kawasaki-reviews-preview-image.PNG "Desktop Demo")

## User Experience

### User stories
As an end-user I want to access the information on this web site with ease, I want to add a review with ease and quick succession. I want to edit my review or any review I feel needs to be updated.

Any employers who visit my site will wannt to see my level of design and consistancy, along with the ability to write functioning code with python3 and mongodb.

Any recruiters who visits my web site will want to see if my site meets the requirments of the position they are recruiting for.

### Strategy

For this project I wanted a motorcycle review site specifically for kawasaki motorcycles. My aim was to evoke a positive emotional response from the user when they visited my site, and provide them with information regarding certain models of kawasaki motorcycles, they coud read reviews from critics, or users, they could edit a user review, delete and add their very own review or a particular model from the set models in the schema.

In this project my goal was to create consistancy in design flow, and colour schemes, as well as showing CRUD functionality. The web site is designed mobile first, in regards to content layout and css media queries, but the site does respond well on desktop, laptop and tablet screens.

The main goal in this project was to showcase my ability to use CRUD functionality, (create, read, update and delete)

### Scope
The scope of the project was to provide an application that the end-user could use while considering what kawasaki motorcycle suites them best and would respond primarily on a mobile device, and showcase my design, python, flask and mongodb skills to date along with html and css.

### Structure
The key aspects of the navbar was to have the navbar fixed to the top of the screen for easy access which allows the user to navigate wherever and whenever.  

In the footer there is some links using the appropriate icons, the email icon which opens up the modal to contact me, and allows the user to contact me via email.

The user reviews, critic reviews, and add a review can be accessed by the navbar. Within the critic reviews section you have all of the set models from the pulled in from database, this schema does not allow the user to edit the critic reviews, as they're critic reviews and should remain on the site, the review details have been sourced from MCN motorcycle review website which is a popular go to site for looking up motorcycles reliablity, engine performance etc.
The critic reviews section has the option to see more details on each particular model of kawasaki motorcycles. This option filters the particular model by its unique id and pulls in more details from the mongo schema.

For the user reviews you are brought to all of the available reviews regardless of dupicates, if I had more time I would have used a similar option to what was used for critic reviews, where you would see an overview of the user reviews, and go to see all particular models. This would then bring you to all the particular models and give you more details. In the user reviews section the user can edit and delete any user review, if I had more time I would have added a popup option asking if the user was sure they wanted to delete the review.

For adding the review the user can only access this by the navbar which means it is allways accessible, I achieved this by means of a popup modal to add a review.

### Skeleton

[Mobile Design wireframe](https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/wireframes/mobile-wireframe.jpg)

[Desktop Design wireframe](https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/wireframes/desktop-wireframe.jpg)

[Critic reviews wireframe](https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/wireframes/critic-reviews.jpg)

[User reviews wireframe](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/wireframes/user-reviews.jpg)

[Add review and edit wireframe](https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/wireframes/add-reviews-and-edit-wireframe.jpg)

[Contact me modal wireframe](https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/wireframes/contact-me-modal-wireframe.jpg)

### Surface

#### Orange shades: 
rgba(224, 87, 8, 0.82);

#### Grey scaled shades are also included within the application.

#222425;

#282929;

#222425f5;

rgba(196, 196, 196, 0.95);

The colour scheme I was going for was to go with the background motorcycle image Kawasaki H2R. This created a pleasing to the eye, and above all evoking a positive response from the end-user.   

## Technologies

1. HTML 5
2. CSS
3. Bootstrap (4.4.1)
4. JavaScript
5. JQuery (3.4.1)
6. Emailjs (2.3.2)
7. Python3
8. Flask (1.1.1)
9. PyMongo (3.10.1)
10. Werkzeug (1.0.0)

## Features
 
### Existing Features

- The core features of my site is to provide information about certain models of kawasaki motorcycles for the user to figure out which bike best suites their needs. The user can add their own review and edit reviews, currently there is no access key required to edit or delete a review, this will be updated in the future, but for this initial release this feature won't be available.

- For my navigation bar I added some jquery to change the colour upon scrolling down through the site. This evokes a positive response from the user and makes it easier to see the navigation elements within the navbar. It is not need before scrolling due to the background colours of the top section of the background image. I also made the navbar fixed to allow constant accessiblity for the user.

- For the footer section I have a contact me logo which bring up a contact me modal form, it also includes social external links to my github and linkedin.

- Within the critics section you can view all particular kawasaki models and you can choose the option `see more` to filter that particular model and show more detiled information from the database.

- For the user reviews you can view all current models within the database and edit or delete any current models. 

- In the navigation bar you can choose the `add review` option and this will bring up a modal and let you add a new review based on the schema of models.

### Features Left to Implement

If I had more time I would like to add a requirement for an access key to edit or delete user reviews, this will be updated in the future, but for this initial release this feature won't be available, as it would result in a fragmented project.
 
I would also like to add the option to filter the users reviews and also have pagination for user reviews, just in case the site receives more traffic in the future, for the moment though this site doesn't have any need for pagination.

## Testing 
Testing ID: test-data-centric-project-eoc
### Tested by: 
Edmund O Callaghan

### Tested devices: 
- DELL Desktop, 
- AMD Desktop, 
- DELL Latitude E5470 Laptop, 
- Fujitsu Q702 Ultra book,
- ZTE Axon 7 Mobile,
- Iphone X, 
- Iphone 6, 
- Samsung S9.

### Tested Resolutions: 
320px x 640px to 4K resolution: 

Note: On 4k screens the site does not support the view height of the screen.  

### Tested Browsers:
- FireFox,
- Google Chrome, 
- Edge. 

- Note: on edge browser the colour of the contact me modal and the add review modal are not supported by edge.
### Code validation Testing:

[Index HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/index-page-validation.PNG)

[Critics Page HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/critics-page-validation.PNG)

[Edit User HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/edit-user-page-validation.PNG)

[User Page HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/user-page-validation.PNG)

[Single Critic Page HTML Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/single-critic-page-validation.PNG)

[Global JavaScript Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/general-js-validation.PNG)

[Send Mail JavaScript Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/send-mail-code-validation.PNG)

[Python Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/python-code-validation.PNG)

[CSS Validation](https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews/blob/master/static/code-validation/css-validation.PNG)

### User stories
For my user stories testing, I had to put myself in the shoes of the user, anyone looking for a quick way to get information about potential kawasaki modals. They would want to see expierenced riders opinons on the matter and detailed descriptions. They would also be looking for more personal and like minded reviews, to get an idea what the everyday rider thinks of these bikes.

The everday user will want to gain access to the applications quickly and will be looking for quick input(s), that give back what they are looking for, like user reviews brings you straight to the reviews at hand, and critic reviews does the same, and the see more option is easy to interpret, which brings you to a detailed review of each particular motorcycle.

They want to be given clean and clear directions as to where they should navigate to in order to achieve their intentions, whether that be sending an email, or adding a review themselves.

As a recruiter or employer I want to find out with quick succession, whether this candidate has the required skills as a database designer/developer for the job spec. When you arrive at the site you are greeted with a professional, concise and impactful website, this showcases good design and clear intentions as to what it is. 

With regards to the above mentioned user stories & the usability of the web app, the outcome for this test was successful, It met all expectations of ease of use. 


### Responsive Flow Testing:

#### Home Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | On Desktop screens the jumbotron stretches out 75% of the screen, the background image is centered | as expected |
| Laptop(s) | On laptop devices it remains the same bar the footer which you now need to scroll down to access | as expected |
| Tablet(s) | On tablet devices the background image is still centered, but the ends of the motorcycle are cut from view and you need to scoll down to view the footer in landscape view | as expected |
| Mobile(s) | On mobile the jumbotron takes up 75% of the width, and the background image is positioned to the center right of the screen, you can't see the footer until you scroll down | as expected |

#### Critics Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | The cards for each review are in rows of 3 | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The cards for each review are in rows of 2 | as expected |
| Mobile(s) | The cards for each review are in rows of 1 | as expected |

**Note:** For user reviews the page behaves the same bar when in mobile view, where there is a small margin around the cards, which is as expected.

#### See more critic review Page

| Element Tested | Expected outcome | Outcome |
| --- | --- | --- |
| Desktop(s) | The card takes up 75% of the screen width and has a scroll option for the detailed description | as expected |
| Laptop(s) | The same as desktop | as expected |
| Tablet(s) | The layout changes where the image stacks on top of the preview description and the overall description stack under the preview description while maintaining the scroll option  | as expected |
| Mobile(s) | The layout remains the same as the tablet bar the content width, which is now 100% of the screen's width. There is no longer a scroll option for the detailed description | as expected |

## Deployment

The project is hosted using heroku as github pages doesn't support mongodb.

In order to deploy your site to heroku you will need to follow these steps:

- If you don't have a heroku account already then please follow this link to sign up. [Heroku sign up](https://signup.heroku.com/login)

- After this step [Heroku sign in](https://id.heroku.com/login)

- Now go to your [Heroku dashboard](https://dashboard.heroku.com)

- From this point you should see an option to the right of the screen called        'New' just under your navigation bar. if you can't find it try this link        [Create new app](https://dashboard.heroku.com/new-app)

- From this point you want to choose a unique name as it won't allow you to         choose one already taken.

- You'll need to set the region for where the servers will be based, so that is up to you, it can be US or EU, if most users willl be from EU, then you should choose EU.

- Click Create app, then you will be brought to the deploy tab.

- Scroll down and you will see 'Deployment method' on your left, from there choose 'Heroku Git'. This has all the commands you'll need to login to heroku via your IDE and deploy/push to heroku.

- In your IDE cli you will need to first login, using command line interface.
    Please type the following into you cli: 
    
    $ heroku login

- You will be asked to press any key from the cli, from this point you will want to do so, and then an external or internal browser will open, which will log you into heroku using the browser or require you to do so if you are currently signed out on your browser, then verify if it was successful.

- Assuming it has been successful, you will want to push/deploy to heroku.

- Before deployment you will need to make sure your procfile, requirements.txt have been created and are up to date in your IDE, if not then please add both to your IDE and then follow the next steps.

        Procfile contents: 'web: python app.py'

        requirements.txt file contents:

            Click==7.0

            dnspython==1.16.0

            Flask==1.1.1

            Flask-PyMongo==2.3.0

            itsdangerous==1.1.0

            pymongo==3.10.1

            Werkzeug==1.0.0


- In order to deploy the site to heroku use the following commands in you cli on your IDE:

    $ git add .

    $ git commit -m "final deployment"

    $ git push heroku master

- After deployment, you still need to setup **config variables**, please follow the instructions below to do so:

    - Go to the '**Heroku Dashboard**' and look for **Settings**.
    - Then click the option to **Reveal Config Vars**.
    - Enter in the variable names and their values
        - Name: **YourSitesURIName** value: Database url here
        - Name: **IP**  value: 0.0.0.0
        - Name: **Port** value: 5000


In order to run the site locally, you can use the clone this site by using the following link in your terminal: `git clone https://github.com/Novicetheaf/data-centric-dev-kawasaki-reviews.git` To remove any connections with Github repository use the following in your terminal: `git remote rm origin`.  

If you need anymore help in cloning this repo, then go to GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).


## MongoDb Schema

### The critic's MongoDB collection `critic reviews` takes the following schema.

{
    "_id": {
        "$oid": "5e63de321c9d440000a20906"
    },

    "image": "",

    "model": "",

    "price": "",

    "engineSize": "",

    "power": "",

    "insuranceGroup": "",

    "seatHeight": "",

    "overallRating": "",

    "overallDescription": "",

    "rideQualityAndBrakes": "",

    "Engine": "",

    "BuildQualityAndReliability": "",

    "InsuranceRunningCostsValue": "",

    "Equipment": ""
}

### The user's MongoDB collection `user reviews` takes the following schema.

{
    "_id": {
        "$oid": "5e63dfe51c9d440000a20907"
    },

    "image": "",

    "model_select": "",

    "overall_rating": "",

    "name": "",

    "ride_quality_and_brakes": "",

    "engine": "",

    "build_quality_and_reliability": "",

    "running_costs_and_value": "",

    "review_summary": ""
}

## Credits

### Media
I used [Pinterest](https://www.pinterest.com/) for my background image, and other motorcycle images.

### Acknowledgements

I used [MCN's site](https://www.motorcyclenews.com/) for my critic reviews content description section, and for general information about each motorcycle that was used in this project.

Modal Contact Form outer sections Reference can be found [here](https://mdbootstrap.com/docs/jquery/modals/forms/)

Bootstrap code I used to look up for reference purposes, I used [bootstrap.com](https://getbootstrap.com/)

**This project is for educational purposes.** 