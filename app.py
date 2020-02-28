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


@app.route('/critic_reviews_search')
def critic_reviews_search():
    return render_template('critic-reviews-search.html', siteReview=mongo.db.siteReview.find())


@app.route('/user_reviews')
def user_reviews():
    return render_template("user-reviews.html", userReviews=mongo.db.ownerReviews.find())


@app.route('/add_review')
def add_review():
    return render_template('add-review.html')


# Sort motorcycles by model

@app.route('/h2r_model')
def h2r_model():
    return render_template('filter-critic-motorcycle-reviews.html',
                           siteReview=mongo.db.siteReview.find
                           ({'model': 'Ninja H2R'}))


@app.route('/vulcan_model')
def vulcan_model():
    return render_template('filter-critic-motorcycle-reviews.html',
                           siteReview=mongo.db.siteReview.find
                           ({'model': 'Vulcan S'}))


@app.route('/zxr_model')
def zxr_model():
    return render_template('filter-critic-motorcycle-reviews.html',
                           siteReview=mongo.db.siteReview.find
                           ({'model': 'ZX-6R'}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)