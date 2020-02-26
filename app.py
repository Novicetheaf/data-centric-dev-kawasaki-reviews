import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'motorcycleReviews'
app.config["MONGO_URI"] = os.environ.get('motorcycleURI')


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/critic_reviews')
def critic_reviews():
    return render_template('critic-reviews.html')


@app.route('/user_reviews')
def user_reviews():
    return render_template("user-reviews.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)