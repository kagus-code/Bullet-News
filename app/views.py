from flask import render_template
from app import app

#Views
@app.route('/')
def index ():
  '''
  View root page function returns the index page
  '''
  title = 'Welcome to Bullet-News'
  return render_template('index.html')

@app.route('/sources/<sources_id>')
def sources(sources_id):
  '''
  View sources page function that returns the sources and details page
  '''
  return render_template('sources.html',id = sources_id)
