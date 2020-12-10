#  import libraries 
# flask t orender template
from flask import Flask, render_template
#Pymongo to interact with Mongo databaase 
from flask_pymongo import PyMongo
# use scraping codeconverted from notebook
import scraping

#set up flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# default HTML page/ homepage route
@app.route("/")
def index():
    #find the mars collection in database 
   mars = mongo.db.mars.find_one()
   # return an html template 
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   # run imported scraping funciton 
   mars_data = scraping.scrape_all()
   #update mars collection with scraped data
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"


if __name__ == "__main__":
    app.run()