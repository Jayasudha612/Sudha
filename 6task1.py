import math
class point():
  pass

p = point()

p.x = (8,9)
p.y = (7,6)

def distance_between_points(a,b):
    dist = ((a[0]-b[0])**2 + (a[1]-b[1])**2)
    print(math.sqrt(dist))

distance_between_points(p.x,p.y)
