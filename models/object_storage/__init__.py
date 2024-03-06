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
  # The ContainerProperties constructor always sets `name` to None,
  # even if name is provided. This is a workaround.
  container_properties = ContainerProperties()
  container_properties.name = container_id
  container_properties.public_access = 'blob'
  container = client.get_container_client(container_properties)
  if container.exists():
    print(' success.')
  else:
    print(f'\nBLOB: Container ({container_id}) does not exist.')
    print(f'BLOB: Creating the container ({container_id})...', end='')
    container.create_container()
    print(' success.')
  return container


client = create_client()
container = get_or_create_container()


from .save_object import save_object
