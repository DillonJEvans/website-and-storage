import os

from azure.storage.blob import BlobServiceClient, ContainerClient, ContainerProperties


def create_client() -> BlobServiceClient:
  """
  Creates the client for connecting to the blob service.
  :returns: The client.
  """
  account_name = os.getenv('BLOB_ACCOUNT_NAME')
  print(f'BLOB: Creating the client ({account_name})...', end='')
  key = os.getenv('BLOB_KEY')
  client = BlobServiceClient(
    account_url=f'https://{account_name}.blob.core.windows.net',
    credential=key
  )
  print(' success.')
  return client


def get_or_create_container() -> ContainerClient:
  """
  Gets the container if it exists, or creates it if it doesn't.
  :returns: The container.
  """
  container_id = os.getenv('BLOB_CONTAINER_ID')
  print(f'BLOB: Getting the container ({container_id})...', end='')
  container = client.get_container_client(container_id)
  if container.exists():
    print(' success.')
  else:
    print(f'\nBLOB: Container ({container_id}) does not exist.')
    print(f'BLOB: Creating the container ({container_id})...', end='')
    container.create_container(public_access='blob')
    print(' success.')
  return container


client = create_client()
container = get_or_create_container()


from .clear_objects import clear_objects
from .save_object import save_object
