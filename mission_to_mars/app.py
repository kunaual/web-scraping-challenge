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

#the below gets listings collection, then it calls scrape_phone (imported) <dot> scrap (it's in the scrap_phone.py file)
#listings.update update whole thing ({}) listings_data, upsert = True  basically doing a merge
@app.route("/scrape")
def scraper():
    mars_infos = mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    listings.update({}, mars_data, upsert=True)  # change this to overwrite
    return redirect("/", code=302)  #go back to index route. w/code 302 which means "found"


if __name__ == "__main__":
    app.run(debug=True)
