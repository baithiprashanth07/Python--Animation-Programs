import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('red')
t.speed(0)
for i in range(110):
    t.circle(190-i,90)
    t.left(90)
    t.circle(190-i,90)
    t.left(18)
    
