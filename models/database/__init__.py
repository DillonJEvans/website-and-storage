import os

from azure.cosmos import CosmosClient, DatabaseProxy, ContainerProxy, PartitionKey


def create_client() -> CosmosClient:
  """
  Creates the client for connecting to Cosmos.
  :returns: The client.
  """
  account_name = os.getenv('COSMOS_ACCOUNT_NAME')
  key = os.getenv('COSMOS_KEY')
  print(f'COSMOS: Creating the client ({account_name})...', end='')
  client = CosmosClient(
    url=f'https://{account_name}.documents.azure.com:443/',
    credential={'masterKey': key}
  )
  print(' success.')
  return client


def get_or_create_database() -> DatabaseProxy:
  """
  Gets the database if it exists, or creates it if it doesn't.
  :returns: The database.
  """
  database_id = os.getenv('COSMOS_DATABASE_ID')
  print(f'COSMOS: Getting/creating the database ({database_id})...', end='')
  database = client.create_database_if_not_exists(database_id)
  print(' success.')
  return database


def get_or_create_container() -> ContainerProxy:
  """
  Gets the container if it exists, or creates it if it doesn't.
  :returns: The container.
  """
  container_id = os.getenv('COSMOS_CONTAINER_ID')
  print(f'COSMOS: Getting/creating the container ({container_id})...', end='')
  container = database.create_container_if_not_exists(
    id=container_id,
    partition_key=PartitionKey('/lastName'),
    offer_throughput=1000,
    unique_key_policy={'uniqueKeys': [{'paths': ['/firstName', '/lastName']}]}
  )
  print(' success.')
  return container


client = create_client()
database = get_or_create_database()
container = get_or_create_container()


from .add_people import add_people
from .clear_people import clear_people
from .query_people import query_people
