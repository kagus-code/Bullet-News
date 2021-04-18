import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the Sources class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_source = Sources(1234,'NTV','Home of first news','https://abcnews.go.com','Genral')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Sources))  
    

