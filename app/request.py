from app import app
import urllib.request,json
from .models import sources
Sources = sources.Sources

#getting api key
apiKey = app.config['NEWS_API_KEY']

#Getting the sources base url
base_url = app.config["SOURCES_API_BASE_URL"]

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
    


