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

r = 10
def draw_circle(t,n):
   for i  in range(n):
    t.fd(r)
    angle = 360/n
    t.lt(angle)


draw_circle(bob,30)

turtle.mainloop()
