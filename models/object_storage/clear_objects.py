from itertools import islice

from . import container


def clear_objects() -> int:
  """
  Clears all objects in the container.
  :returns: The number of objects deleted.
  """
  print(f'BLOB: Clearing the container ({container.container_name})...')
  blob_names = container.list_blob_names()
  deleted = 0
  # Delete the blobs in batches of 256.
  # 256 is the maximum number of blobs that can be deleted in one `delete_blobs()` request.
  while True:
    blob_batch = list(islice(blob_names, 256))
    # If the batch to delete is empty, then all blobs have been deleted.
    if len(blob_batch) == 0:
      break
    # Delete the batch.
    print(f'      Deleting {len(blob_batch):,} objects starting at index {deleted:,}...', end='')
    container.delete_blobs(*blob_batch)
    deleted += len(blob_batch)
    print(' success.')
  print(f'BLOB: Deleted {deleted:,} objects from the container ({container.container_name}).')
  return deleted
