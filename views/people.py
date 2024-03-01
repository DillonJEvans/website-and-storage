from . import app

@app.route('/')
def index():
  return 'This is a test!'
