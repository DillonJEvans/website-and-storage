from azure.cosmos import CosmosClient, PartitionKey
from flask import Flask

import config


app = Flask(__name__)
app.json.sort_keys = False

client = CosmosClient(config.COSMOS_HOST, {'masterKey': config.COSMOS_KEY})
database = client.create_database_if_not_exists(config.COSMOS_DATABASE_ID)
container = database.create_container_if_not_exists(
  config.COSMOS_CONTAINER_ID,
  PartitionKey('/lastName'),
  offer_throughput=1000,
  unique_key_policy={'uniqueKeys': [{'paths': ['/firstName', '/lastName']}]}
)


import models
import views
