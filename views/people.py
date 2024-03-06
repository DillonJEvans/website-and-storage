import requests
from flask import request

from . import app
from models import add_people, clear_people, query_people, save_object


@app.get('/people')
def get_people():
  return query_people(request.args)


@app.post('/people')
def post_people():
  file_url = 'https://css490.blob.core.windows.net/lab4/input.txt'
  with requests.get(file_url) as people:
    add_people(people.text)
    object_url = save_object('input.txt', people.text)
  return object_url


@app.delete('/people')
def delete_people():
  clear_people()
  return '', 204
