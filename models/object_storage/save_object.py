from azure.storage.blob import ContentSettings

from . import container


def save_object(name: str, data: bytes | str, content_type='text/plain') -> str:
  """
  Saves the object to object storage.
  :param name: The name to save the object as.
  :param data: The data to save to the object.
  :param content_type: The content type of the object.
  :returns: The URL of the object.
  """
  # azure.core.exceptions.ResourceNotFoundError
  blob = container.upload_blob(
    name=name,
    data=data,
    overwrite=True,
    content_settings=ContentSettings(content_type=content_type)
  )
  return blob.url
