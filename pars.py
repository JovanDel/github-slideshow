import urllib2
from xml.etree import ElementTree

url = ("http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML")
s = urllib2.urlopen(url)
print (s)
