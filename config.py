import os
class Config:
    '''
    General configuration parent class
    '''
    SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    ARTICLE_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}  