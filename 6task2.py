class rect():
   pass

class point():
   pass 

r = rect()
r.width = 100
r.height = 200
point.corner = (0,0)

def find_center(a,b,c):
  print(((a-c[0])/2),((b - c[1])/2))
  

find_center(r.width,r.height,point.corner)
