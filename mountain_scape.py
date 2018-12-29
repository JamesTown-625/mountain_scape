import random
import turtle

startX = 50
startY = 50

def rec_func(x, y, p):
    
    if x <= -7 and y <= -7: 
        p.penup()
        return rec_func(50.25,50,p)
    elif x >= 107 and y <= -7:
        return "done"
    elif x >= 50.25:
        p.goto(x, y)
        x = p.xcor() + random.randrange(1,7)
        y = p.ycor() - random.randrange(1,7)
        p.pendown()
        return rec_func(x,y,p)
    else:
        p.pendown()
        p.goto(x, y)
        x = p.xcor() - random.randrange(1,7)
        y = p.ycor() - random.randrange(1,7)
        p.penup()
        return rec_func(x, y, p)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.setworldcoordinates(0,0,100,100)
    p = turtle.Turtle()
    p.color('brown')
    p.pensize(2.5)
    p.penup()
    p.goto(startX, startY)
    p.pendown()
    rec_func(startX,startY,p)
    wn.exitonclick()

if __name__ == '__main__':
    main()