import turtle
from turtle import *

class Player(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=20
        self.y=50
        self.dy=self.y
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
        self.dy = self.y+15

    def duck(self):
        x = self.xcor()
        y = self.ycor()
        self.dy = self.y-15

    def move(self):
        self.goto(self.x, self.dy)
        if self.dy!=self.y:
            self.dy=self.y







