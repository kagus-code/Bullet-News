class Sources :
  '''
  Sources class to define Sources object
  '''
  def __init__(self,id,name,description,url,category):
    self.id = id
    self.name = name
    self.description = description
    self.url =url
    self.category = category

class Article :
  '''
  Articles class to define articles object
  '''

  def __init__(self,image,description,time,url):
    self.image = image
    self.description = description
    self.time = time
    self.url = url
