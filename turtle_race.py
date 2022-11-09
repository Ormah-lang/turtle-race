from turtle import Turtle
from turtle import mainloop
from random import randint


# create some instances of a Turtle object
lizzy = Turtle()
rik = Turtle()
brie = Turtle()
hondo = Turtle()

# attributes of lizzy
lizzy.color('red')
lizzy.shape('turtle')
lizzy.penup()
lizzy.goto(-160, 100)
lizzy.pendown()

# attributes of rik
rik.color('green')
rik.shape('turtle')
rik.penup()
rik.goto(-160, 70)
rik.pendown()

# attributes of brie
brie.color('purple')
brie.shape('turtle')
brie.penup()
brie.goto(-160, 40)
brie.pendown()

# attribute of hondo
hondo.color('blue')
hondo.shape('turtle')
hondo.penup()
hondo.goto(-160, 10)
hondo.pendown()


# This makes all turtles to move forward randomly
for movement in range(100):
    lizzy.forward(randint(1, 5))
    rik.forward(randint(1, 5))
    brie.forward(randint(1, 5))
    hondo.forward(randint(1, 5))


mainloop()
