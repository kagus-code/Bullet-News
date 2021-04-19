import urllib.request,json
from .models import Sources
from .models import Article


#getting api key
apiKey = None


#Getting the sources base url
base_url = None
article_url = None


def configure_request(app):
    global apiKey,base_url,article_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config["SOURCES_API_BASE_URL"]
    article_url = app.config["ARTICLE_BASE_URL"]

def get_sources():
  '''
  Function that gets the json response to the url request
  '''
  get_sources_url = base_url.format(apiKey)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_results(sources_results_list)

  return sources_results    

def process_results(sources_list):
  '''
  function that processes sources results
  '''
  sources_results = []
  for sources_item in sources_list:
    id = sources_item.get('id')
    name = sources_item.get('name')
    description = sources_item.get('description')
    url=sources_item.get('url')
    category=sources_item.get('category')
    sources_object = Sources(id,name,description,url,category)
    sources_results.append(sources_object)


  return sources_results  

def get_articles(source):
  get_article_url = article_url.format(source,apiKey)

  with urllib.request.urlopen(get_article_url) as url:
    article_data = url.read()
    article_data_response = json.loads(article_data)

    article_results =None

    if article_data_response['articles']:
      article_result_list = article_data_response['articles']
      article_results = process_articles(article_result_list)

  return article_results

def process_articles(article_list):
  '''
  function that processes the article result and transorm them to a list of objects 
  '''

  article_results = []

  for article_item in article_list:
    image = article_item.get('urlToImage')
    description = article_item.get('description')
    time = article_item.get('publishedAt')
    url = article_item.get('url')

    if image:
        article_object = Article(image,description,time,url)
        article_results.append(article_object)

  return article_results




    

    


