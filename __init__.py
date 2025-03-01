from flask import Flask
app = Flask(__name__)

# Import routes and the db initialization function
import flaskr.main
from flaskr import db

# Call the function to create the Cars table if it doesn't exist
db.create_Cars_table()
