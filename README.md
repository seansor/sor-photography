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



### Wireframes & Database Entity Relationship Diagrams

Wireframes and the Database Entity Relationship Diagram for the site are provided
in the project files in the "wireframes_erd" folder.

## Features

### Existing Features



### Features Left to Implement




## Technologies Used

#### HTML5
#### CSS3
#### Javascript

#### Bootstrap
The project uses [bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) to assist in layout
and styling. [Bootswatch](https://bootswatch.com/3/) was used to implement a particular bootstrap theme.

#### Fontawesome
The [Fontawesome](https://fontawesome.com/) icon toolkit was used to add icons to the website.

#### JQuery
The project uses [JQuery 3.4.1](https://jquery.com/) to simplify DOM manipulation.

#### Python
The backend of the application is built using [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

#### Unittest

Python's [unittest](https://docs.python.org/3/library/unittest.html) framework was used for testing.


## Testing



### Registration



### Login Page


### Products Page


### Product Page


### Add Recipe Page



### Edit Recipe



### Responsiveness
The site was tested on different devices including a windows laptop, an IOS device
(iPhone 6) and an android device (OnePlus Phone). The website was also testing
using different browsers including Edge, Firefox and Chrome and the developer
tools in these browsers were also used to test the website's responsiveness.

The website displays well on all sizes of device. On small screen sizes
the photographs and forms take up close to 100% of the screen width and less content 
is shown in certain instances as designed.


### Bugs


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
on heroku, going to settings and adding the variables to CONFIG VARS. The configuration 
variables for this project are: MONGO_URI, SECRET_KEY, PORT, and IP address. I also
set a DEBUG config var so that I can always have the application running in debug 
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

### Acknowledgements

. 
