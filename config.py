import os
from typing import Dict


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
