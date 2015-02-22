class Spikes_top(Turtle):
    def __init__(self):
        RawTurtle.__init__(self,canvas)
        self.x=200 #the edge of the screen
        self.y=100
        self.hight=50
        self.width=15


class Spikes_bottom(Turtle):
    def __init__(self):
        RawTurtle.__init__(self,canvas)
        self.x=200 #the edge of the screen
        self.y=0
        self.hight=50
        self.width=15