import turtle
from turtle import *

class Player(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=20
        self.y=50
        self.score=0
        self.hight=45
        self.width=20
        self.goto(self.x,self.y)
        self.shape("arrow")
        self.pencolor("red")
        self.speed(3)



    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return 8
   
    def jump(self):
        x = self.xcor()
        y = self.ycor()
        print("hey")
        self.goto(x,y+50)
        self.goto(x,y)

    def duck(self):
        self.goto(x,y-50)
        self.goto(x,y)



