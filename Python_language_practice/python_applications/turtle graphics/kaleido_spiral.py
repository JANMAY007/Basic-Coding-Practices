import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','orange','yellow','blue','green','purple'])

def draw_circle(size,angle,shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 10,angle+1,shift+0.5)

t.bgcolor('black')
t.speed(1000)
t.pensize(4)

draw_circle(30,0,1)

ti.sleep(1)
t.hideturtle()
t.done()