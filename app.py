from flask import Flask
from dotenv import load_dotenv


# Load environment variables, but don't override any existing variables
# (to allow environment variables set for the Azure Web App to be used).
load_dotenv(override=False)


# Create the app.
app = Flask(__name__)
app.json.sort_keys = False


import models
import views
