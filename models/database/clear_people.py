import os

from azure.cosmos import PartitionKey

from . import database, container


def clear_people() -> None:
  """
  Clears the database.
  """
  global container
  database.delete_container(container)
  container = database.create_container_if_not_exists(
    os.getenv('COSMOS_CONTAINER_ID'),
    PartitionKey('/lastName'),
    offer_throughput=1000,
    unique_key_policy={'uniqueKeys': [{'paths': ['/firstName', '/lastName']}]}
  )
