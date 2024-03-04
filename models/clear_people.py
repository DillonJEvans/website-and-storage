import os

from azure.cosmos import PartitionKey

import models
from . import database


def clear_database() -> None:
  """
  Clears the database.
  """
  database.delete_container(models.container)
  models.container = database.create_container_if_not_exists(
    os.getenv('COSMOS_CONTAINER_ID'),
    PartitionKey('/lastName'),
    offer_throughput=1000,
    unique_key_policy={'uniqueKeys': [{'paths': ['/firstName', '/lastName']}]}
  )
