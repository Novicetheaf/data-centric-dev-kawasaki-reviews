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

[Mobile Design wireframe - Income Tax Calculator](https://github.com/Novicetheaf/interactive-frontend-development-project/blob/master/wireframes/income-tax-calc-wireframe-mobile.pdf)

[Mobile Design wireframe - Miles Per Gallon Calculator](https://github.com/Novicetheaf/interactive-frontend-development-project/blob/master/wireframes/mpg-calc-wireframe-mobile.pdf)

[Desktop Design wireframe](https://github.com/Novicetheaf/interactive-frontend-development-project/blob/master/wireframes/desktop-wireframe-design.pdf)

[Modal Design wireframe](https://github.com/Novicetheaf/interactive-frontend-development-project/blob/master/wireframes/modal-wireframe.pdf)

### Surface

#### Red shades: 
`rgb(102, 10, 10);`

`rgba(138, 58, 58);`

`rgb(199, 60, 60);`

`rgb(196, 23, 23);`

#### Cream/White shades: 
`rgb(199, 235, 224);`

`rgb(255, 245, 245);`

`rgb(255, 255, 255);`

#### Grey scaled shades are also included within the application.

The colour scheme I was going for is this web application was to match up with a impactful contrast, yet pleasing to the eye, and above all evoking a positive response from the end-user.   

## Technologies

1. HTML 5
2. CSS
3. Bootstrap (4.4.1)
4. JavaScript
5. JQuery (3.4.1)
6. Emailjs (2.3.2)

## Features
 
### Existing Features

- The core features of my site is to make life easier for the end-user, by solving calculations for them and giving them specifically simplified results, that make it quick and easy to use. 

- For my navigation bar I added a dropdown button with a jquery toggle arrow. This slides down content and give te user more options only if they want them, it keeps the flow simple, and evoking positive emotional response with clean consistancy in flow and design.

- My web apps I used an accordion bootstrap setup, and implemented jquery to fixed on application to be open at once, so that the user doesn't have to scroll down very far to navigate the site.

- For the income tax calculator section I used used simple input and dropdown options along with a calculate tax button, when clicked would perform the calculations to output taxed amount for the year, net pay for the year, and a weekly pay output.

- The other web app miles per gallon calculator also keeps with the same format of styling. It uses two input box's miles/kilometers and your fuel used in litres. 
It also has a required dropdown option as to wether your distance is in miles or kilometers, this then changes the output text below accordingly.
It also features radio buttons to change the gallon rate to US(3.75L) or UK(4.25L). It also follows the same styled calculate button which takes your inputs and calculates them below in MPG(miles per gallon).

### Features Left to Implement

If I had more time I would like to use Chart.js to create a pie chart based on the output values to give a nice visual comparison of the what you pay on tax's vs what you received for the year etc.

I still have two applications left to add to this toolkit, the first one would be a stopwatch. The second application would be a calorie counter.  

## Testing 
Testing ID: test-interactive-frontend-project-eoc
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

- Note Axon 7 mini:

no issues found, bar in mobile view the text output was too large to fit in one line, depending on the output size for income tax calculator, this issue was resolved by changing the set text size lower on that particular output section, and setting it to go back to normal when the screen size get to a min of 400px, this was achieved using media queries to respond to larger screens, thus remaining mobile first.

### Tested Browsers:
- FireFox,
- Google Chrome, 
- Edge. 

- Note: on edge browser getting footer links blue, as oppsed to red, and contact me is black as opposed to red.
- This issue has been resolved, I added a support for Edge browsers to use hex colors codes, which rectified the issue.

### Code validation Testing:
[CSS Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/css-validation.PNG)

[HTML Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/html-validation.PNG)

[Global JavaScript Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/global-code-validation.PNG)

[Income Tax Calc JavaScript Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/income-tax-code-validation.PNG)

[MPG Calc JavaScript Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/mpg-calc-code-validation.PNG)

[Send Mail JavaScript Validation](https://github.com/novicetheaf/interactive-frontend-development-project/blob/master/assets/code-validation/send-mail-code-validation.PNG)

### User stories
For my user stories testing, I had to put myself in the shoes of the user, anyone looking for a quick way to calculate income or fuel consumption and employers/recruiters. The user will know straight away that this site is a toolkit, it solves and simplifies. 

The everday user will want to gain access to either of the two applications quickly and will be looking for a concise response in regards to their input(s). They want to be given clean and clear directions as to where they should navigate to in order to achieve their intentions, whether that be sending an email, or using the application themselves.

As a recruiter or employer I want to find out with quick succession, whether this candidate has the required skills as an interactive frontend designer/developer for the job spec. When you arrive at the site you are greeted with a professional, concise and impactful website, this showcases good design and clear intentions as to what it is. 

With regards to the above mentioned user stories & the usability of the web app, the outcome for this test was successful, It met all expectations of ease of use. 

Note: For the accordion this uses bootstrap by standard as part of the template, however, with this in mind you have the option to close both applications down, and for design reasons, and lack of content, my idea was to keep one card section open at all time, so for this I had to write custom jquery to keep one application open.
Ontop of this I also added in jquery to keep only one section open at once, so that the user does not have to scroll down if they open two at the same time it will close the other one.


### Responsive Flow Testing:

#### **Expected outcome for Desktop(s):**  
On desktop devices the background image appears and covers all background space correctly. The navigation section takes up the full with of the screen, and also becomes semi transparent in order to show the background. The main content section remains fixed to 768px, the footer section remains within these confinements also.

- Site Remains responsive throughout all devices that were tested.
#### Actual outcome:
- On desktop screens the site responds the same as above.

#### **Expected outcome for Laptop(s):** 
Elements behave the same as on desktop, other then the background image that become more streched, yet not losing any pixel quailty of the image.
- The Site Remains responsive throughout all devices that were tested. 
#### Actual outcome:
On Laptop screens the site responds the same as above.

#### **Expected outcome for Tablet(s):**  
Elements behave the same as on latop and desktop, bar the background image cannot be seen from 768px down, other then behind the navigation section as it remains transparent for this resolution also.

- Site Remains responsive throughout all devices that were tested.

#### Actual outcome:
On Tablet screens the site responds the same as above.

#### **Expected outcome for Mobile(s):**  
the background image is no longer visible as the media query that set it in motion only comes into effect at a min 600px. The linkedin and github social icons in the navigation bar get push to the left of the section. The content adjusts accordingly with the screen size of the mobile devices tested, bar the not made above in regards to the output text for the income tax calculator, which was rectified. Please see resolution section of testing for more information.

Other then the above issue the site remains responsive throughout all devices that were tested. 
#### Actual outcome:
On Mobile screens the site responds the same as above.


### Automation Testing: 

- For this section I choose to use Selenium GUI based automation tests.

-  I choose automation testing to test the functionality of the website. Please see the seperate section on automation to run the tests and to get information on running the tests also. 

[Automation Test Case, Files & How To Setup](https://github.com/Novicetheaf/interactive-frontend-development-project/tree/master/automation-tests)

Selenium is the most popular and widely used open source gui testing platform. For my tests I was between two minds to use C# Selenium Web driver or the quick and easy Selenium IDE, which is an extension for you FireFox browser. Selenium Webdriver is more extendable and gives you more control over how your tests can interact and at what speed and they also generally make for more stable and reliable test cases. 

The benefit of using Selenium IDE over the C# based Webdriver, is simply time, Selenium IDE is faster to get up off the ground, and generally is used for small scale applications, it is actully better then C# when it comes to simple sites that don't have to many varients, and not a lot of updates, 

If I do get to build upon this application in the future I will probably transfer over to the Webdriver as it is far easier to make extensible, but for the moment considering the limited time constraints, this is the best solution.

For the test cases for my automation I simply went through every element of functionality.

Note on testing:
- This did actully find one small issue where if the user adds numbers and letters, with numbers first and letters following, the result is 'NaN'.
Fixed this issue was resolved by changing the javascript to check the length of charactors for input fields. 

### Unit Testing: 

For this project I didn't do any true unit testing, though I did test each block of code prior to commiting each part, within the short time constraints doing true unit testing would slow the project down considerably, and would have resulted in an incomplete project.

## Deployment

The project is hosted using heroku as github pages doesn't support mongodb.

In order to deploy your site to heroku you will need to follow these steps:

- If you don't have a heroku account already then please follow this link to        sign up. [Heroku sign up](https://signup.heroku.com/login)

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


## Credits

### Media
I used [Ljndawson's site](http://ljndawson.org/2560x1440-white-wallpaper-hd.html) for my background image.

### Acknowledgements

Modal Contact Form outer sections Reference can be found [here](https://mdbootstrap.com/docs/jquery/modals/forms/)

Bootstrap code I used to look up for reference purposes, I used [bootstrap.com](https://getbootstrap.com/)

**This project is for educational purposes.** 