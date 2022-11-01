import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
def d(x,y):
    t.up()
    t.goto(x,y)
    t.down()
d(-30,30)
a=22
for i in range(180):
    for i in range(i):
        t.pencolor('red')
        t.rt(6)
        t.circle(a)
        a=a+0.5
turtle.done()

