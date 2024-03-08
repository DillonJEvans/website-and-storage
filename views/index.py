from flask import render_template

from . import app


@app.route('/')
def index():
  return render_template('index.html.j2', title='CSS436 P4')
