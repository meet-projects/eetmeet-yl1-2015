import turtle
from turtle import *

class Spikes_top(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=200 #the edge of the screen
        self.y=70
        self.hight=50
        self.width=20
        self.goto(self.x,self.y)
        #self.shape("spikesT.gif")- FIX THIS
        
    def move(self,speed):
        x = self.xcor() # this line gives me the current x cordination of the astroid and saves it in variable x
        y = self.ycor() # this line gives me the current y cordination of the astroid and saves it in variable y
        self.goto(x-speed,y)
        if x-speed <= 0:
            self.goto(self.x,self.y)

    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return self.width/2

class Spikes_bottom(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.x=200 
        self.y=30
        self.hight=50
        self.width=15
        #self.shape("spikesB.gif")- FIX THIS
        self.goto(self.x,self.y)
    
    def move(self,speed):
        x = self.xcor() # this line gives me the current x cordination of the spikes and saves it in variable x
        y = self.ycor() # this line gives me the current y cordination of the spikes and saves it in variable y
<<<<<<< HEAD

        
        self.goto(x,y)

=======
        self.goto(x-speed,y)
>>>>>>> b90aa65695ede8b2af837b5e5d9924eb8d9a29be
        if x-speed <= 0:
            self.goto(self.x,self.y)

    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return self.width/2

