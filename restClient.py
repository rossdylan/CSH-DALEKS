import urllib2
from urllib import urlencode
import time

urllib2.urlopen('http://tula.student.rit.edu/engage',data=urlencode({'derp':'herp'}))

urllib2.urlopen('http://tula.student.rit.edu/backward',data=urlencode({'derp':'herp'}))

time.sleep(1)

urllib2.urlopen('http://tula.student.rit.edu/stop',data=urlencode({'derp':'herp'}))
