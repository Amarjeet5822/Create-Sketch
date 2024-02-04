# by using turtle Library drawing an area
import turtle
myStar = turtle.Turtle()
turtle.speed(1000)
myStar.right(75)
myStar.forward(100)
for i in range(5):
    myStar.right(144)
    myStar.circle(30)
    myStar.color("red")
    myStar.fillcolor("red")    
    myStar.forward(100)
    myStar.circle(30)
turtle.done()
