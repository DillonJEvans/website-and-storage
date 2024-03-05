import os

from azure.cosmos import CosmosClient, PartitionKey
from flask import Flask
from dotenv import load_dotenv


# Load environment variables, but don't override any existing variables
# (to allow environment variables set for the Azure Web App to be used).
load_dotenv(override=False)


# Create the app.
app = Flask(__name__)
app.json.sort_keys = False

# Create the cosmos client.
client = CosmosClient(os.getenv('COSMOS_HOST'), {'masterKey': os.getenv('COSMOS_KEY')})
# Get (or create) the cosmos database.
database = client.create_database_if_not_exists(os.getenv('COSMOS_DATABASE_ID'))
# Get (or create) the cosmos container.
container = database.create_container_if_not_exists(
  os.getenv('COSMOS_CONTAINER_ID'),
  PartitionKey('/lastName'),
  offer_throughput=1000,
  unique_key_policy={'uniqueKeys': [{'paths': ['/firstName', '/lastName']}]}
)


import models
import views
