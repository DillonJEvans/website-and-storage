from azure.cosmos import CosmosClient, PartitionKey
from flask import Flask

import config


# Create the app.
app = Flask(__name__)
app.json.sort_keys = False

# Create the cosmos client.
client = CosmosClient(config.COSMOS_HOST, {'masterKey': config.COSMOS_KEY})
# Get (or create) the cosmos database.
database = client.create_database_if_not_exists(config.COSMOS_DATABASE_ID)
# Get (or create) the cosmos container.
container = database.create_container_if_not_exists(
  config.COSMOS_CONTAINER_ID,
  PartitionKey('/lastName'),
  offer_throughput=1000,
  unique_key_policy={'uniqueKeys': [{'paths': ['/firstName', '/lastName']}]}
)


import models
import views
