
import turtle, time, math

s = turtle.getscreen()

earth = turtle.Turtle()
earth.shape("circle")
earth.color("green", "black")
moon = turtle.Turtle()
moon.color("black")
moon.shape("circle")
# 
g = 6.674**-11
m1 = 5.972**10
m2 = 7.34767309**6
r2 = 400.400/10

f = g*((m1*m2)/r2)
moon.pen(speed=10)
# moon.forward(30)
moon.goto(0, -r2)
# moon.left(-90)
x = True
while x:
    # moon.circle(f)
    moon.circle(f)
    moon.begin_poly()
    turtle.title(f"{moon.position()}")
    moon.position()
time.sleep(2)