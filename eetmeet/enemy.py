class Enemy(Turtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.x=200
        self.y=20
        self.hight=35
        self.width=20

    def move(self,speed):
        x = self.xcor() # this line gives me the current x cordination of the astroid and saves it in variable x
        y = self.ycor() # this line gives me the current y cordination of the astroid and saves it in variable y
        slef.goto(x-speed,y)

    def getSize(self):
        return self.hight*self.width

    def getRadius(self):
        return 8