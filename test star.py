import turtle as t
import random as r

def star(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    size = r.randint(15,30)
    
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

t.bgcolor('black')
t.color('yellow')
t.ht()
t.speed(10)

t.onscreenclick(star)

t.listen()
#t.mainloop()
