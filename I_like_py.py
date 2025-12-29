import turtle as t
import math

PETALS = 12
RADIUS = 90
SWEEP = 60
STEM_LEN = 220

BG = "#FFFFFF"
PETAL_OUTLINE = "#FF4F7B"
PETAL_FILL = "#FFA3B1"
CENTER_FILL = "#FFD166"
STEM_COLOR = "#2E8B57"
LEAF_FILL = "#7BD389"
LEAF_RADIUS = 46
LEAF_SWEEP = 70

t.bgcolor(BG)
t.speed(0)
t.hideturtle()


def petal(radius, sweep):
    t.color(PETAL_OUTLINE, PETAL_FILL)
    t.begin_fill()
    t.circle(radius, sweep)
    t.left(180 - sweep)
    t.circle(radius, sweep)
    t.end_fill()
    t.right(180 - sweep)


def flower(petals=12, radius=90, sweep=60):
    for _ in range(petals):
        petal(radius, sweep)
        t.right(360 / petals)


def center(dot_size=38):
    t.up()
    t.goto(20, 100)
    t.down()
    t.color(PETAL_OUTLINE, CENTER_FILL)
    t.begin_fill()
    t.circle(dot_size / 2)
    t.end_fill()


def stem(length=200):
    t.up()
    t.goto(0, 100)
    t.setheading(-90)
    t.forward(20)
    t.down()
    t.color(STEM_COLOR)
    t.pensize(8)
    t.forward(length)


def leaf(radius=LEAF_RADIUS, sweep=LEAF_SWEEP, offset=90, side=1):
    t.color(STEM_COLOR, LEAF_FILL)
    t.pensize(2)
    t.up()
    t.goto(0, 100 - offset)
    t.setheading(-90 + side * 40)
    t.down()
    t.begin_fill()
    t.circle(radius, sweep)
    t.left(180 - sweep)
    t.circle(radius, sweep)
    t.end_fill()


t.up()
t.goto(0, 100)
t.setheading(90)
t.down()

flower(PETALS, RADIUS, SWEEP)

center(40)

stem(STEM_LEN)
leaf(offset=120, side=1)
leaf(offset=170, side=-1)

t.done()
