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
    return render_template("user-reviews.html", userReview=mongo.db.ownerReviews.find())


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


# add review

@app.route('/insert_review', methods=['POST'])
def insert_review():
    userReview=mongo.db.ownerReviews

    model_select = request.form['model_select']
    overall_rating = request.form['overall_rating']
    name = request.form['name']
    ride_quality_and_brakes = request.form['ride_quality_and_brakes']
    engine = request.form['engine']
    build_quality_and_reliability = request.form['build_quality_and_reliability']
    running_costs_and_value = request.form['running_costs_and_value']
    review_summary = request.form['review_summary']

    review_form = {
        'model_select': model_select,
        'overall_rating': overall_rating,
        'name': name,
        'ride_quality_and_brakes': ride_quality_and_brakes,
        'engine': engine,
        'build_quality_and_reliability': build_quality_and_reliability,
        'running_costs_and_value': running_costs_and_value,
        'review_summary': review_summary
    }

    userReview.insert_one(review_form)
    return redirect(url_for('user_reviews'))


# delete user review

@app.route('/remove_review/<review_id>')
def remove_review(review_id):

    mongo.db.ownerReviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('user_reviews'))


# Edit Recipe

@app.route('/edit_page_review/<review_id>')
def edit_reviews(review_id):
    userReview = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template('edit-review.html', review=userReview)


@app.route('/edit_review/<review_id>', methods=['POST'])
def edit_review(review_id):
    userReview = mongo.db.ownerReviews

    model_select = request.form['model_select']
    overall_rating = request.form['overall_rating']
    name = request.form['name']
    ride_quality_and_brakes = request.form['ride_quality_and_brakes']
    engine = request.form['engine']
    build_quality_and_reliability = request.form[
        'build_quality_and_reliability']
    running_costs_and_value = request.form['running_costs_and_value']
    review_summary = request.form['review_summary']

    userReview.update({'_id': ObjectId(review_id)}, {
        'model_select': model_select,
        'overall_rating': overall_rating,
        'name': name,
        'ride_quality_and_brakes': ride_quality_and_brakes,
        'engine': engine,
        'build_quality_and_reliability': build_quality_and_reliability,
        'running_costs_and_value': running_costs_and_value,
        'review_summary': review_summary
    })

    return redirect(url_for('user_reviews'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
