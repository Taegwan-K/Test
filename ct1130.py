import turtle
import random

def draw(x,y): #도형 그리는 함수
    turtle.penup() #펜 들기
    turtle.goto(x,y) #마우스 클릭 좌표로 이동
    turtle.pendown() #펜 놓기

    size_num = random.randint(1,3) #사이즈 랜덤한 세가지 중 하나
    
    if size_num == 1: 
        size = 40
    elif size_num == 2:
        size = 60
    else:
        size = 80

    color_num = random.randint(1,3) #색 랜덤한 세가지 중 하나
    
    if color_num == 1:
        color = 'red'
    elif color_num == 2:
        color = 'blue'
    else:
        color = 'green'

    turtle.color(color) #펜 색 바꾸기
    
    if shape == 1: #삼각형 그리기
        turtle.begin_fill()
        turtle.right(random.randint(1,360))
        for i in range(4):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()
        
    elif shape == 2: #사각형 그리기
        turtle.begin_fill()
        turtle.right(random.randint(1,360))
        for i in range(5):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()
        
    elif shape == 3: #원 그리기
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

#예외 처리를 위해 1,2,3만 입력 받을 수 있게 함
try:
    num = int(input("1.삼각형 2.사각형 3.원 :"))
    sh = [1,2,3]
    shape = sh[num-1]
    
except Exception:
    print("잘못된 수") #예외 일 때 출력
else:
    turtle.speed(100)
    turtle.onscreenclick(draw) #클릭한 위치에 도형 그리기

    turtle.listen() #이벤트 감지
