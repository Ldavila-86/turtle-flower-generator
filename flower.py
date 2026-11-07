import turtle
import math
import random

random.seed(7)


screen = turtle.Screen()
screen.setup(width=800, height=480)
screen.bgcolor("#12001c")  #sets a color for background with color name

t = turtle.Turtle()
t.speed(0)

def stars():
    t.penup()
    for _ in range(70):
        x = random.randint(-390, 390)
        y = random.randint(-230, 230)
        t.goto(x, y)
        t.dot(random.randint(2, 4), "white")  #draws a dot with random size and color white

def stem():
    t.penup()
    t.goto(0, 60)
    t.setheading(-72)
    t.color("#2ecc71")
    t.pensize(7)
    t.pendown()
    t.circle(-420,34)  #draws a circle with radius -420 and extent 34 degrees

def leaf(x, y, angle):  
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.color("#7bed9f", "#2ed573")  #sets the color for edge and fill of leaves
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    t.circle(95, 60)  #draws a circle with radius 95 and extent 60 degrees
    t.left(120)
    t.circle(95, 60)  #draws a circle with radius 95 and extent 60 degrees
    t.end_fill()

def petal(size, edge, fill):
    t.color(edge, fill)
    t.pensize(2)
    t.begin_fill()
    t.circle(size, 80)  #draws a circle with radius size and extent 80 degrees
    t.left(100)
    t.circle(size, 80)  #draws a circle with radius size and extent 80 degrees
    t.left(100)
    t.end_fill()

def bloom():
    rings = [
    (8, 120, "#8b1e5a", "#b12f73"),
    (8, 102, "#b12f73", "#d94b9c"),
    (7, 84, "#d94b9c", "#ff6bb5"),
    (6, 66, "#ff6bb5", "#ff85c2"),
    (5, 50, "#ff85c2", "#ffb3d9"),
    (4, 34, "#ffb3d9", "#ffe0ef")
]
    for count, size, edge, fill in rings:
        shift = random.randint(0, 40)
        for i in range(count):
            t.penup()
            t.goto(0, 60)
            a = shift + i * (360 / count)
            t.setheading(a + random.uniform(-4, 4))
            t.pendown()
            s = size * random.uniform(0.94, 1.04)
            petal(s, edge, fill)

def center():
    t.penup()
    t.goto(0, 60)
    t.dot(26, "#ffd54f")
    t.dot(5, "#f4b400")
    for i in range(14):
        a = math.radians(i * 360 /14)
        x = math.cos(a) * 20
        y = 60 + math.sin(a) * 20
        t.goto(x, y)
        t.dot(5, "orange")


stars()
stem()
leaf(12, -40, 15)
leaf(13, -110, 165)
bloom()
center()
t.hideturtle()
turtle.done()
        





