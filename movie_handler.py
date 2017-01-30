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
    with open('data.json', 'a') as outfile:
      # for k, v in self.dic.items():
         json.dump(self.dic, outfile)
      #   outfile.write('\n')


  def characters( self, content ):
    if self.isInCommonElement == "type":
      self.type = content
    elif self.isInCommonElement == "description":
      self.description = content


#factory method to create a parser
  # create an XMLReader
parser = xml.sax.make_parser()

#put content handler in the parser
parser.setContentHandler( MovieHandler() )

#finally call the parse method of the xml interface, passing file name
parser.parse("movies.xml")

  # make into normal python object using normal
  # data structures, most likely strings
  # https://www.tutorialspoint.com/python/python_xml_processing.htm

  # then pass the python object into an json parser


