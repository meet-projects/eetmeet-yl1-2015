import turtle
from turtle import *

class Player(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=20
        self.y=50
        self.dy=0
        self.score=0
        self.hight=45
        self.width=20
        self.goto(self.x,self.y)
        self.shape("Character.gif")
        #self.speed(1)
        self.countup=0
        self.countdown=0
        self.up = False
        self.down = False


    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return 8
   
    def jump(self):
        self.up = True
        self.dy = 15
        self.countup = 0

    def duck(self):
        self.down = True
        self.dy = -15
        self.countdown = 0

    def move(self):
        
        self.goto(self.xcor(), self.y+self.dy)

        #this is to make the player jump and return to it's place afterwards
        if self.up:
            if self.countup < 100:
                self.countup = self.countup + 1
            elif self.countup < 200:
                if self.dy > 0:
                    self.dy = 0
                self.countup = self.countup + 1
            else:
                self.dy = 0
                self.countup = 0
                self.up = False

        #this is to make the player duck and return to it's place afterwards
        if self.down:
            if self.countdown < 100:
                self.countdown = self.countdown + 1
            elif self.countdown < 200:
                if self.dy < 0:
                    self.dy = 0
                self.countdown = self.countdown + 1
            else:
                self.dy = 0
                self.countudown = 0
                self.down = False







