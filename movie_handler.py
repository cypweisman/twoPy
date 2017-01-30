import xml.sax

class MovieHandler( xml.sax.ContentHandler ):

  def __init__(self):
    self.isInCommonElement = ""
    self.title = ""
    self.description = ""
    self.type = ""

  def startElement( self, tag, attributes ):
    self.isInCommonElement = tag
    if tag == "movie":
      self.title = attributes["title"]
      print self.title

  def endElement( self, tag ):
    if self.isInCommonElement == "type":
      print self.type
    elif self.isInCommonElement == "description":
      print self.description

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


