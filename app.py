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

# links to images for user reviews and critic reviews

h2r_image = "https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/2018-Kawasaki-Ninja-H2R1.jpg"
vulcan_s_image = "https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/2017-Kawasaki-Vulcan-S-ABS-Cafe-Review-5.jpg"
versys_image = "https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/2019-kawasaki-versys-1000-se-lt-corner.jpg"
zx6r_image = "https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/20_ZX6R-krt-hero1-scaled.jpeg"
klr_650_image = "https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/KawasakiKLR6502016_060-768x512.jpg"
z900_image = "https://raw.githubusercontent.com/Novicetheaf/data-centric-dev-kawasaki-reviews/master/static/images/g-000221-g_W2210131_11-kawasaki-z900-636982140121390902.jpg"

# go to index page

@app.route('/')
def index():
    return render_template("index.html")

# go to critic reviews page

@app.route('/critic_reviews_search')
def critic_reviews_search():
    return render_template('critic-reviews-search.html',
                           siteReview=mongo.db.siteReview.find())

# go to user reviews page

@app.route('/user_reviews')
def user_reviews():
    return render_template("user-reviews.html",
                           userReview=mongo.db.ownerReviews.find())


# get more details on a particular motorcycle and filter by its id

@app.route('/show_more/<review_id>')
def show_more(review_id):
    return render_template('single-critic-motorcycle-review.html',
                           siteReview=mongo.db.siteReview.
                           find({'_id': ObjectId(review_id)}))


# add review

@app.route('/add_review')
def add_review():
    return render_template('add-review.html')


@app.route('/insert_review', methods=['POST'])
def insert_review():
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

    if model_select == "H2R":
        image = h2r_image

    elif model_select == "Vulcan S":
        image = vulcan_s_image

    elif model_select == "KLR 650":
        image = klr_650_image

    elif model_select == "Z900":
        image = z900_image

    elif model_select == "Versys 1000":
        image = versys_image

    elif model_select == "ZX-6R":
        image = zx6r_image

    review_form = {
        'model_select': model_select,
        'overall_rating': overall_rating,
        'name': name,
        'ride_quality_and_brakes': ride_quality_and_brakes,
        'engine': engine,
        'build_quality_and_reliability': build_quality_and_reliability,
        'running_costs_and_value': running_costs_and_value,
        'review_summary': review_summary,
        'image': image
    }

    userReview.insert_one(review_form)
    return redirect(url_for('user_reviews'))


# Delete user review

@app.route('/remove_review/<review_id>')
def remove_review(review_id):

    mongo.db.ownerReviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('user_reviews'))


# Edit review

@app.route('/edit_review/<review_id>', methods=['GET'])
def edit_review(review_id):
    userReview = mongo.db.ownerReviews.find_one({"_id": ObjectId(review_id)})
    return render_template('edit-review.html', review=userReview)


@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
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

    if model_select == "H2R":
        image = h2r_image

    elif model_select == "Vulcan S":
        image = vulcan_s_image

    elif model_select == "KLR 650":
        image = klr_650_image

    elif model_select == "Z900":
        image = z900_image

    elif model_select == "Versys 1000":
        image = versys_image

    elif model_select == "ZX-6R":
        image = zx6r_image

    userReview.update({'_id': ObjectId(review_id)}, {
        'image': image,
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
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=False)
