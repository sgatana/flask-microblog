# Getting started
A blog application developed in flask micro-framework
## Installation
Install to your local machine by cloning the repo

``git clone https://github.com/sgatana/flask-microblog.git ``
## Database Setup
to set database use 

``SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL)``

## Running the application
set the environment to run the application

```
export FLASK_CONFIG=development

export SECRET_KEY='this-is-very-secret'

export DB_URL='postgresql://postgres@username:password/-databasenname-'
```