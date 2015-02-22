class Player(Turtle):
    def __init__(self):
        RawTurtle.__init__(self,canvas)
        self.x=20
        self.y=50 
        self.score=0
        self.speed=3
        self.hight=45
        self.width=20

   
	def jump(self):
    	self.goto(x,y+50)
    	self.goto(x,y)

    def duck(self):
    	self.goto(x,y-50)
    	self.goto(x,y)



