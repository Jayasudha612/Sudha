import math
class point():
  pass

p = point()

p.x = (0,9)
p.y = (7,8)

def new_point(a,b):
    dist1 = (a[0]+b[0])
    dist2 = (a[1]+b[1])
    print(dist1,dist2)

new_point(p.x,p.y)
