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
        self.shape("Character.gif")
        self.speed(1)



    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return 8
   
    def jump(self):
        self.x = self.xcor()
        self.y = self.ycor()
        self.y = self.y+1

    def duck(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x,y-25)
        self.goto(x,y)

    def move(self):
        self.goto(self.x, self.y)



