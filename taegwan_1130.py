import turtle as t
import random as r

def draw(x,y,shape):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    size = r.randint(15,30)
    
    if shape == 1: #삼각형
        t.right(r.randint(1,360))
        for i in range(4):
            t.forward(size)
            t.left(120)
    
    elif shape == 2: #사각형
        t.right(r.randint(1,360))
        for i in range(5):
            t.forward(size)
            t.left(90)

    elif shape == 3: #원
            t.circle(size)
    else:
        IndexError

color_arr = ['red','blue','green']
color = color_arr[r.randint(0,2)]
    
try:
    shape = int(input("1.삼각형 2.사각형 3.원 : "))
except shape!=1 & shape!=2 & shape != 3:
    print("올바른 수를 입력하세요.")
else:

    
    t=t.pen()
    t.color(color_arr[r.randint(0,2)])
    t.ht()
    t.speed(10)

    t.onscreenclick(draw)

    t.listen()
    #t.mainloop()
