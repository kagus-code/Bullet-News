import unittest
from app.models import Article

class ArticlesTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the Article class
  '''
  def setUp(self):
    '''
    set up method that will run before article test
    '''
    self.new_article = Article('https://ichef.bbci.co.uk/news/1024/branded_news/DAE7/production/_118093065_navalnyfeb202021reuters.jpg','birth of prince george','2021-04-17T19:52:18.331743Z','http://www.bbc.co.uk/news/world-europe-56786266')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Article))  

