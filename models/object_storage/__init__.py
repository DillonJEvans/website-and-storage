import os

from azure.storage.blob import BlobServiceClient


# Create the blob client.
print('Connecting to the blob service...', end='')
client = BlobServiceClient(
  account_url=f'https://{os.getenv("BLOB_ACCOUNT_NAME")}.blob.core.windows.net',
  credential={'account_name': os.getenv('BLOB_ACCOUNT_NAME'), 'account_key': os.getenv('BLOB_KEY')}
)
print(' connected.')
# Get or create the blob container.
# public_access='blob'????
print('Getting the blob container...', end='')
container = client.get_container_client(os.getenv('BLOB_CONTAINER_ID'))
if container.exists():
  print(' blob container retrieved.')
else:
  print('\nBlob container does not exist.')
  print('Creating the blob container...', end='')
  container.create_container()
  print(' blob container created.')


from .save_object import save_object
