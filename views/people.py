import requests
from flask import request

from . import app
from models import add_people_to_database, query_people


@app.get('/people')
def get_people():
  return query_people(request.args)


@app.post('/people')
def post_people():
  file_url = 'https://css490.blob.core.windows.net/lab4/input.txt'
  with requests.get(file_url) as people:
    add_people_to_database(people.text)
  return ''


@app.delete('/people')
def delete_people():
  return '', 404
  # return '', clear_database()
