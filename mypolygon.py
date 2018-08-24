import turtle
import math

bob = turtle.Turtle()

def square(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

def polygon(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)

def circle(t, r):
    for i in range(50):
        t.fd(r/(2*math.pi))
        t.lt(360/50)

def circle2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    l = circumference / n
    polygon(t, l, n)

square(bob, 100)
polygon(bob, 50, 6)
circle(bob, 120)
turtle.mainloop()