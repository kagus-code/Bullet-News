from flask import render_template
from app import app
from .request import get_sources
from .request import get_articles

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

@app.route('/article/<source>')
def articles(source):
  '''
  View articles page function that returns the articles and details page
  '''
  source_article = get_articles(source)
  print(source_article)

  return render_template('article.html',news=source_article)
