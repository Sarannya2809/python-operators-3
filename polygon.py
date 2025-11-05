import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon= turtle.Turtle()
Num_sides= 6
side_legnth = 70
angle = 360.0 / Num_sides
for i in range(Num_sides):
    polygon.forward(side_legnth)
    polygon.right(angle)
turtle.done()