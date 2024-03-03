import os
from typing import Dict


# Fill in the COSMOS_DEFAULT dictionary with the information about your cosmos database.
# HOST = The URI of the database.
# KEY  = The key to the database.
# DATABASE_ID  = The name of the database. This will be created if it does not exist.
# CONTAINER_ID = The name of the container. This will be created if it does not exist.
#
# Both the HOST and KEY can be found on the Azure management console.
#   1. Go to the Azure Cosmos DB service.
#   2. Select (or create) your Azure Cosmos DB account.
#   3. On the left-hand side, under "Settings", select "Keys".
# HOST is the "URI" on that page.
# KEY is the "PRIMARY KEY" (or "SECONDARY KEY") on that page.

COSMOS_DEFAULT: Dict[str, str] = {
  'HOST': '',
  'KEY': '',
  'DATABASE_ID': '436p4',
  'CONTAINER_ID': 'people'
}


COSMOS: Dict[str, str] = {
  'HOST': os.environ.get('ACCOUNT_HOST', COSMOS_DEFAULT['HOST']),
  'KEY': os.environ.get('ACCOUNT_KEY', COSMOS_DEFAULT['KEY']),
  'DATABASE_ID': os.environ.get('COSMOS_DATABASE', COSMOS_DEFAULT['DATABASE_ID']),
  'CONTAINER_ID': os.environ.get('COSMOS_CONTAINER', COSMOS_DEFAULT['CONTAINER_ID'])
}

COSMOS_HOST: str = COSMOS['HOST']
COSMOS_KEY: str = COSMOS['KEY']
COSMOS_DATABASE_ID: str = COSMOS['DATABASE_ID']
COSMOS_CONTAINER_ID: str = COSMOS['CONTAINER_ID']
