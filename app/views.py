from flask import render_template
from app import app
from .request import get_sources

#Views
@app.route('/')
def index ():
  '''
  View root page function returns the index page
  '''
  #Getting sources
  all_sources = get_sources()
  print(all_sources)
  title = 'Welcome to Bullet-News'
  return render_template('index.html',title=title,sources = all_sources)

@app.route('/sources/<sources_id>')
def sources(sources_id):
  '''
  View sources page function that returns the sources and details page
  '''
  return render_template('sources.html',id = sources_id)
