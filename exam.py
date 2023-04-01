import turtle as t
import random

size_list = [20,40,60]
color_list = ["red","blue","yellow"]

def draw(x,y):
    t.penup()
    t.goto(x,y)
    a = random.randint(0,359)
    size = size_list[random.randint(0,2)]
    color = color_list[random.randint(0,2)]
    t.color(color)
    t.right(a)
    t.pendown()
    if shape == 1:
        t.begin_fill()
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.end_fill()
    elif shape == 2:
        t.begin_fill()
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.end_fill()
    else:
        t.begin_fill()
        t.circle(size)
        t.end_fill()

        
try:
    sh_lis = [1,2,3]
    shape = sh_lis[int(input("1.사각형 2.삼각형 3.원 : "))-1]
    
except IndexError:
    print("잘못된 입력입니다.")

else:
    #스크린 객체 생성
    screen = t.Screen()
#스크린 배경색 지정
    screen.bgcolor("black")
    t.speed(1000)
    t.onscreenclick(draw) #클릭한 위치에 도형 그리기

    t.listen() #이벤트 감지

