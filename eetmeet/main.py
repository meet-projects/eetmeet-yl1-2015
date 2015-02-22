import turtle 
import Player(Turtle)
import canvas

screenMinX = 0
screenMinY = 0
screenMaxX = 200
screenMaxY = 100

def intersect (Player,Spikes_top):

def intersect (Player,Spikes_bottom):


def intersect(object1,object2):
        dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
        
        radius1 = object1.getRadius()
        radius2 = object2.getRadius()
       
        if dist <= radius1+radius2:
            return True
        else:
            return False


turtle.mainloop 