import sys
import xml.sax
from movie_handler import MovieHandler

path = raw_input("Please enter path of xml file:")

#factory method to create a parser
parser = xml.sax.make_parser()

#put content handler in the parser
parser.setContentHandler( MovieHandler() )

#finally call the parse method of the xml interface, passing file name
parser.parse(path)

#example
#XFiles/movies.xml