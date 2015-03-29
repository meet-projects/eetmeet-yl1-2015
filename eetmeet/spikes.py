import turtle
from turtle import *

class Spikes_top(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=200 #the edge of the screen
        self.y=100
        self.hight=50
        self.width=15
        self.goto(self.x,self.y)
        self.speed(5)
        
    def move(self,speed):
        x = self.xcor() # this line gives me the current x cordination of the astroid and saves it in variable x
        y = self.ycor() # this line gives me the current y cordination of the astroid and saves it in variable y
        if x-speed <= 0:
            self.ht()
            self.goto(self.x,self.y)
            self.st()
        self.goto(x-speed,y)

    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return self.width/2

class Spikes_bottom(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=200 #the edge of the screen
        self.y=0
        self.hight=50
        self.width=15
        self.goto(self.x,self.y)
        self.speed(5)
    
    def move(self,speed):
        x = self.xcor() # this line gives me the current x cordination of the spikes and saves it in variable x
        y = self.ycor() # this line gives me the current y cordination of the spikes and saves it in variable y
        if x-speed <= 0:
            self.ht()
            self.goto(self.x,self.y)
            self.st()
        self.goto(x-speed,y)


    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return self.width/2

