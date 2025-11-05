import turtle
t=turtle.Turtle()
t.color("gold")
t.pensize(3)
t.speed(5)
for _ in range(3):
    t.forward(100)
    t.left(120)
t.right(60)
t.forward(50)
for _ in range(3):
    t.forward(100)
    t.right(120)
turtle.done()