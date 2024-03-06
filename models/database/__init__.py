import os

from azure.cosmos import CosmosClient, PartitionKey


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


from .add_people import add_people
from .clear_people import clear_people
from .query_people import query_people
