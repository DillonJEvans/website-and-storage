from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
from flask import Flask

app = Flask(__name__)
app.json.sort_keys = False

endpoint = 'https://436p4.documents.azure.com:443/'

credential = DefaultAzureCredential()
client = CosmosClient(url=endpoint, credential=credential)

database = client.get_database_client('436p4')
people_container = database.get_container_client('people')

import models
import views
