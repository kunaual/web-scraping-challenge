from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline  another way single line
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars_infos = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_stuff=mars_infos)

#
#mars_infos.update upsert = True will update matching document, if none matching will inset new.
@app.route("/scrape")
def scraper():
    print('----scrape 1 ------------------------------------------------------------------')
    mars_infos = mongo.db.mars_info
    print('----scrape 2 ------------------------------------------------------------------')
    mars_data = scrape_mars.scrape()
    print('----scrape 3 ------------------------------------------------------------------')
    mars_infos.update({}, mars_data, upsert=True)  
    return redirect("/", code=302)  #go back to index route. w/code 302 which means "found"


if __name__ == "__main__":
    app.run(debug=True)
