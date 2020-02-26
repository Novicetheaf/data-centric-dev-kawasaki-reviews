import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'motorcycleReviews'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@eoccluster-jcwib.mongodb.net/motorcycleReviews?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('critic-reviews.html', categories=mongo.db.categories.find())