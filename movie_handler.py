import xml.sax
import json

class MovieHandler( xml.sax.ContentHandler ):

  def __init__(self):
    self.isInCommonElement = ""
    self.title = ""
    self.description = ""
    self.type = ""
    self.dic = dict()

  # def asdict(self, *keys):
  #   if not keys:
  #       keys = ['self.title', 'self.description', 'self.type']
  #   return dict((key, getattr(self, key)) for key in keys)

  def startElement( self, tag, attributes ):
    self.isInCommonElement = tag
    if tag == "movie":
      self.title = attributes["title"]
      self.dic['title'] = self.title
      print self.title

  def endElement( self, tag ):
    if self.isInCommonElement == "type":
      self.dic['type'] = self.type
      print self.type
    elif self.isInCommonElement == "description":
      self.dic['description'] = self.description
      print self.description
    if (self.description != "\n") and (len(self.dic) == 3):
      with open('JFiles/movies.json', 'a') as outfile:
           json.dump(self.dic, outfile, indent=2)

  def characters( self, content ):
    if self.isInCommonElement == "type":
      self.type = content
    elif self.isInCommonElement == "description":
      self.description = content

 # @classmethod
  # def addToG(self):
  #   if (self.description != null) and (self.description != "\n"):
  #     gdic.append(self.dic)








