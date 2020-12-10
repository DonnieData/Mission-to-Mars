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

