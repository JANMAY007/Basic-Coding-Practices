import turtle as t
t.penup()
t.speed(1)
#t.goto(0,-100)#for circle
t.goto(-100,100)#for square
t.pendown()
#square
t.color('red')
for i in range(1,5):
    t.forward(200)
    t.right(90)
#circle
t.speed(100)
t.color('blue')
for i in range(1,181):
    t.circle(i+90)
    t.left(1)
#star
t.penup()
t.goto(200,200)
t.pendown()
t.speed(1)
t.color('red')
for i in range(1,9):
    t.forward(150)
    t.left(135)
t.done()