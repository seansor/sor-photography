# SOR Photography

[![Build Status](https://travis-ci.org/seansor/sor-photography.svg?branch=master)](https://travis-ci.org/seansor/sor-photography)

## A website to purchase photos taken by SOR Photography or to request 
## commissions

This website allows users to purchase photographs from any of SOR Photography's
featured collections or to request specially commissioned photographs.

## UX

The website has a minimalist and sleek design with a largely monotone colour
palatte so that the photographs are the centre of attention. Site navigation and
forms aim to be easy to understand and intuitive to any user. The site makes
use of icons and infographics to give users visual as well as written direction.
Users are given active feedback through the use of unobstrusive messages, which 
may indicate a successful transcation or a prohibited action.

### User Stories

Regular user:
* As a user I want to be able to see the latest featured collection of photos I 
  can purchase.
* As a user I want to be able to see a back-catalog of photos that I can purchase.
* As a user I want to be able to make multiple purchases at once.
* As a user I want to see a summary of my items before proceeding to the checkout.
* As a user I want to be able to edit the items I have selected for purchase,
  increasing, decreasing the amount or removing the item altogether.
* As a user looking for a custom artwork/photo I want to be able to request this 
  from the site administrator.
* I want to receive a quote price for the work which I can review and then accept 
  or reject.
* As a user I want to have my own personal profile which will show me my account 
  details (if I have signed up) and where I can view my previous product puchases
  as well as manage my commission requests.

Site Admin:
* As a site administrator I should have all of the same capabilities as a regular 
  user as explored above, as well as additional administrator priveleges and 
  capabilities.
* As a site admin I should be able to see all the requests for commissions.
* I want to be able to provide a quote price for the requested commissions.
* I want to be able to manage all data entries from the admin panel, including 
  viewing all product orders and billing/shipping information for each user.


### Wireframes & Database Entity Relationship Diagrams

Wireframes and the Database Entity Relationship Diagram for the site are provided
in the project files in the "wireframes_erd" folder.

## Features

### Existing Features

* On the home page a user can see all of the featured collections. The current 
  series is displayed by a carousel which moves automatically every few seconds
  to show the next photo. Users can also scroll through the photos manually by 
  clicking on the direction arrows.
* Thumbnails of the the back-catalog of collections are shown below the current 
  series. The user can click on any one of these thumbnails and that collection 
  will enlarge, and the user can then scroll through that collection or see all 
  items in the collection by clicking the 'panelling' button.
* Users can choose to puchase any of these photos at which stage they will be 
  redirected to the individual product and the product options available to them.
  Each product is offered in a variety of size and prices.
* A user can select any of the photo options to purchase and they will be added 
  to a cart.
* The cart will keep track of the items selected and the associated quantity and 
  price.
* If the user wishes to puchase the items in their cart, i.e. proceed to checkout, 
  they will need to login or create an account. If they click on checkout and are 
  not logged in they will be redirected to the login page.
* If a user is already registered they can simply login by entering either their 
  username or email and password and clicking on "Login".
* A user that tries to login who is not registered will recieve feedback to that
  effect.
* A user that is already registed, that tries to register again will recieve 
  feedback asking them to log in.
* A user that has forgotten their password can request to reset it from the login 
  page. They will receive an email to the email account they signed up with with 
  instructions to reset it.
* A user that is not logged in can browse photos and add them to cart as described 
  above but not purchase them. Neither can a user that is not logged in, request a 
  commission, i.e. a user must have an account and be signed in to do this.
* Signed in users can request commissions. Once a quote is provided by a site admin, 
  this quote and order will show up in the users profile and give them the option 
  to either accept or reject the quote. Accepted quotes will remain in their order 
  history. Rejected quotes will be removed.
* Users can also see their puchase history in their profile by expanding the 
  purchase history dialog.
* Admin Users can review all requests for commissions from the main site (i.e.
  do not need to access django admin) and provide quotes for the works from here.
* Icon badges indicate to users when they have items in their cart or when a quote 
  is waiting to be responded to.
* Cart items will persist for users that remain logged in for two weeks before 
  being removed. Non-logged in users will lose the cart items when they close their 
  browsers.


### Features Left to Implement

* Showcase of previously commissioned works if customer consents.
* Eventually as the database grows, on a date of issue basis, old quotes/orders and 
  history of product purchases should be moved to another database.


## Technologies Used

#### HTML5
#### CSS3
#### Javascript

#### Python
The backend of the application is built using [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

#### Django
[Django 2.2.6](https://www.djangoproject.com/) web application framework was used to assist in the backend development.

#### JQuery
The project uses [JQuery 3.4.1](https://jquery.com/) to simplify DOM manipulation.

#### Amazon S3
[Amazon S3](https://aws.amazon.com/s3/) is used to store the static and media files for the project.

#### Bootstrap
The project uses [bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) to assist in layout
and styling. [Bootswatch](https://bootswatch.com/3/) was used to implement a particular bootstrap theme.

#### Fontawesome
The [Fontawesome](https://fontawesome.com/) icon toolkit was used to add icons to the website.

#### FancyBox
The [FancyBox](http://fancybox.net/home) tool was used for displaying the collection images,
in a Mac-style "lightbox" that floats overtop of web page.

#### Unittest

Python's [unittest](https://docs.python.org/3/library/unittest.html) framework was used for testing. This testing 
framework is integrated with teh django framework.

#### Python-dotenv
[python-dotenv==0.10.3](https://pypi.org/project/python-dotenv/) was used to hide configuration variables.



## Testing
Python's [unittest](https://docs.python.org/3/library/unittest.html) framework was used for automated testing.
The tests for each app can be found in the applications folder in the test.py file.
The automated testing is still being worked on so coverage is currently not extensive 
but a certain amount of automated testing was developed for each app. The checkout 
app has the most comprehensve test suite.
Many of the views have automated testing to ensure they render the correct page
with a http 200 Ok response. As explained above test coverage is still being worked 
on but any testing not currently covered by automated testing has be manaully tested 
extensively. The tests for each app can be run by typing
"`./manage.py test <app_name>.tests`" into the bash console (if running on linux).

### Registration
Creates user correctly.
Prevents already registered email and username from being used.

### Login Page
Renders correctly.
Allows users to login with either username or password.
Prevents login when either is incorrect.

### Password Reset
Renders correctly.
Password reset works correctly. Reset instructions recieved to entered email 
address and new password confirm resets it.

### Index/Products Page
Renders correctly.
Carousel for current series works.
FancyBox displays other collections correctly.
Purchase links work and redirect to product page.

### Product Page
Renders correctly.
Size selection and Qty selection work correctly.
User prevented from proceeding if either is not entered.
Add to cart button adds the correct product and qty to cart.

### Cart Page
Renders correctly.
Cart tracks cart items correctly, keeping track of the items, qty and price.

### Checkout
Renders correctly.
Allows user to enter billing/shipping info. Remembers previous users and autofills 
if "remember me" option is selected.

Stripe payment works correctly.
Correctly creates OrderInfo database entry and OrderLineItem database entry.

### Commission request
Renders correctly.
Form correctly creates Order database entry.

### Requested Commissions/Orders Page
Renders correctly.
Shows correct orders and order information.
Allows Admin user to provide quote.

### Quotes Page
Renders correctly
Allows admin user to provide price for works.
Creates correct Quote database entry.

### Profile Page
Renders correctly.
Shows user information.
Shows requested commissions and allows users to accept or reject.
Shows product order history correctly.


### Responsiveness
The site was tested on different devices including a windows laptop, an IOS device
(iPhone 6) and an android device (OnePlus Phone). The website was also testing
using different browsers including Edge, Firefox and Chrome and the developer
tools in these browsers were also used to test the website's responsiveness.

The website displays well on all sizes of device. On small screen sizes
the photographs and forms take up close to 100% of the screen width and less content 
is shown in certain instances as designed. Larger tables have the ability to scroll 
horizontally on small devices.

### Bugs
No known bugs at this stage but the writing of automated testing is ongoing.


## Deployment
This site is hosted using Heroku, deployed directly from the master branch.
To deploy I set up a new new app in my [heroku dashboard](https://dashboard.heroku.com/apps).
I installed heroku CLI using the "`sudo snap install --classic heroku`" in the bash
terminal. I then logged in the heroku using the "heroku login" command and entered
my credentials. The heroku app gets it's files from git so it must be linked to 
the git repository. To do this I ran the command "`heroku git:remote -a sor-photography`".
Then in order to push any changes commited to the git repository to the heroku
server I used the command "`git push heroku master`" in the bash terminal.
In order for the application to run on the heroku server the configuration
variables need to be set in the heroku app. These were set by accessing the project 
on heroku, going to settings and adding the variables to CONFIG VARS. The main
configuration variables for this project are:
    * AWS_ACCESS_KEY_ID (for storage of static/media files on Amazon S3)
    * AWS_SECRET_ACCESS_KEY (for storage of static/media files on Amazon S3)
    * DATABASE_URL (The PostgreSQL add on is used on heroku as the database)
    * EMAIL_ADDRESS (For Password Reset capability)
    * EMAIL_PASSWORD (For Password Reset capability)
    * HOSTNAME
    * SECRET_KEY
    * STRIPE_PUBLISHABLE_KEY (For Stripe payment form)
    * STRIPE_SECRET_KEY (For Stripe payment form)
I also set a DEBUG config var so that I can always have the application running in debug 
when developing and not have to remember to change it to DEBUG=FALSE for deployment.

To run locally, you can clone this repository directly into the editor of your
choice by pasting '`git clone https://github.com/seansor/sor-photography.git`'
into your terminal. To cut ties with this GitHub repository, type "`git remote
rm origin`" into the terminal.

#### Dependencies
It should be noted that this python project has a number of dependencies all of which 
are listed in the requirements.txt file in the main project folder. To ensure that 
only the dependencies needed are included in the requirements.txt file a virtual 
environment was set up of the project. This also ensures that the correct version 
of these packages is used for this project and updates to packages outside of the 
virtual environment will nto affect this projects dependencies. It is recommended
that anyone intending to clone this project and work on it locally should first
create a vitual environment. There is a built-in package in python called [venv](https://docs.python.org/3.6/library/venv.html#module-venv) 
which provides support for creating lightweight “virtual environments” with their
own site directories, optionally isolated from system site directories.
In order to use this module you should be using python 3.3 or higher. Nothing needs 
to be installed to run the venv package, it is part of the standard library.
To create a new virtual environment (in linux or mac) navigate to the folder you 
want the VE to be created in. (It is recommended to put this in the main project 
folder but note that the projetc files should not go inside the venv folder created.
The VE should be able to be disposed of without affected the project files.)
Type the following command: "`python3 -m venv project_name`". As a convention my VE
was called venv so the command was "`python3 -m venv venv`". This will create a new 
folder venv. To activate the virtual env type source project_name/bin/activate. 
In this VE you can now install the required dependencies. So to create the 
requirements.txt file with the dependencies listed you can run "`pip freeze`" and 
redirect to requirements.txt by entering `pip freeze > requirements.txt`.


## Credits

### Content
The majority of the code is created by me. There is some code that has been taken
from STRIPE's website for the payment form functionality. This is clearly marked in 
the stripe.js file in the /static/js folder.

If a user has an issue with any of the media/images illustrated on the site and 
feels that copyright has been infringed upon, please do not hesitate to contact 
me via GitHub and I will remove the relevant content.

### Acknowledgements
The Django documentation was used extensively as a resource for the creation of this 
project.

 
