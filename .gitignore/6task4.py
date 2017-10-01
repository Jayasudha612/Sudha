import math
import turtle
bob = turtle.Turtle()


def draw_rect(t):
  t.fd(100)
  t.lt(90)
  t.fd(60)
  t.lt(90)
  t.fd(100)
  t.lt(90)
  t.fd(60)

draw_rect(bob)

def circle(t,r):
   circum = 2*math.pi*r
   n = int((circum) / 2)
   length = circum / n
   angle = 360/n
   for i in range(n):
    t.fd(length)
    t.lt(angle)



circle(bob,100)


turtle.mainloop()
