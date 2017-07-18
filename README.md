# FlaskWebApp

I have made a simple web application to manage Restaurants and their Menu Items.
For this application I have used the Python coding language along with Flask web framework. 
The database is PostgreSQL and I have used Flask-SQLAlchemy as the ORM to connect to the database.

```
python version = 3.5.2
flask version = 0.12.2
flask-SQLAlchemy = 2.2
psycopg2 = 2.6.2
```

I have used PyCharm Community edition as my IDE of choice for development and pgAdmin4 as GUI for the database.


This application allows users to view/add/edit/delete restaurants and their associated Menu Items. The database schema is two tables - Restaurant and MenuItem having One-to-Many relationship and linked via a ForeignKey.
To run the application on your system 
1. Fork/Download the project to your system
2. Setup the required environments (python 3.5.x, Flask, Flask-SQLAlchemy, PostgreSQL and psycopg2)
3. run `database_setup.py`
4. run `populate_db.py`
5. run `app.py`
6. Open the application on `localhost:5000`


The emphasis of this project was to learn the concepts of Web Development and Web Applications - making the database, using ORMs,
performing CURD operations, undersstand URL routing, GET/POST requests and setting up a simple front end to show the results.

Ideas for further enhancements are to add API end points, setup login using OAuth and design a fancy UI using CSS.
