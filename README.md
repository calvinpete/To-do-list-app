
[![Build Status](https://travis-ci.org/calvinpete/To-do-list-app.svg?branch=Flask)](https://travis-ci.org/calvinpete/To-do-list-app)    [![Coverage Status](https://img.shields.io/coveralls/github/calvinpete/To-do-list-app/Flask.svg)](https://coveralls.io/github/calvinpete/To-do-list-app?branch=Flask)   [![Test Coverage](https://api.codeclimate.com/v1/badges/fd5b8c13551753d5a7d1/test_coverage)](https://codeclimate.com/github/calvinpete/To-do-list-app/test_coverage)

# To-Do list API Endpoints

The api endpoints enable you to create an account, login, create a to do list, add a task, remove a task, delete all tasks view all to do lists created, mark a task as finished, un mark an incomplete task and recover a deleted task

## Getting Started

To run the application, make sure you have the following installed on your local machine.

### Prerequisites

```
Git
Python 3.6.3
Flask
JSON Web tokens
Virtual Enviroment
```

### Starting the application

Clone the project by running this in the terminal

```
git clone https://github.com/calvinpete/To-do-list-app/tree/Flask
```

Activate the virtualenv by running this command in the terminal

```
source venv/bin/activate
```

Install the packages.

```
pip install -r requirements.txt
```

Run the application in the terminal

```
python3 run.py
```

## Running the tests

Run this command in the terminal

```
python3 -m unittest -v
```

### Running tests with coverage

You can run tests with coverage by running this command in the terminal

```
nosetests --with-coverage --cover-package=app
```

### Features

|               Endpoint                           |          Functionality      |
| -------------------------------------------------|:---------------------------:|
| POST /auth/register                              | Create an account           |
| POST /auth/login                                 | Login                       |
| POST /tasks                                      | Create a To do List         |
| POST /task/title                                 | Add a task                  |
| DELETE /tasks/title/taskId                       | Delete a task               |
| DELETE /tasks/title                              | Delete all tasks            |
| PUT /tasks/title/taskId                          | Mark finished task          |
| PUT /tasks/finished/title/taskId                 | Un mark finished task       |
| PUT /tasks/title/recycle_binID/former_taskId     | Recover deleted task        |



## Deployment

The app is deployed on this [link](https://todo-list-appv1.herokuapp.com/api/v1/)

## Built With

* [Python 3.6.3](https://www.python.org/) - General Purpose Language
* [Flask](http://flask.pocoo.org/) - Python Micro Web Framework
## Authors

Calvin Tinka

## License
This app is open source hence free to all users
