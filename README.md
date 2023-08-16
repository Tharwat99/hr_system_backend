# hr system backend rest apis

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tharwat99/hr_system_backend_django.git
$ cd hr_system_backend_django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Then makemigrations and migrate models to sqlite db:
```sh
(env)$ python manage.py makemigrations 
(env)$ python manage.py migrate
```

You should create .env file in hr_system dir and add three variables inside it:

**Note:** Create a SECRET_KEY value for your app by running the following command at a terminal prompt: python -c 'import secrets; print(secrets.token_hex())'.

```sh
SECRET_KEY = "<put_your_secret_key_here>"
DEBUG = True
ALLOWED_HOSTS = '*'
```
Once `pip` has finished downloading the dependencies and create .env and add the required variables:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```
