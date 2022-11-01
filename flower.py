import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('orange')
t.speed(0)
for i in range(180):
    t.circle(190-1,90)
    t.left(90)
    t.circle(190-i,90)
    t.left(18)

