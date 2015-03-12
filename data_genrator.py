# When you want to have multiple urls for say
  For zoomlevel=6 x=2^z-1 and y=2^z-1
  Below program will give you a list of all the possible combinations for x and y in the url 

__author__ = 'deshmuda'
for i in range(63):
    for j in range(63):
        print 'http://myurl'"%d"%i+'&y='"%d"%j+'&zoomLevel=6'
