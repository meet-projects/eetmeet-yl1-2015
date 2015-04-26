from turtle import *
from playerClass import Player
from spikes import Spikes_top
from spikes import Spikes_bottom
import tkinter.messagebox
import tkinter
import random
import math

screenMinX = 0
screenMinY = 0
screenMaxX = 200
screenMaxY = 100



def intersect(object1,object2):
       
        dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
        
        radius1 = object1.getRadius()
        radius2 = object2.getRadius()
       
        if dist <= radius1+radius2:
            return True
        else:
            return False
def main():
	# These 4 lines just to prepare the window of the game, no need to change them
	root = tkinter.Tk()
	root.title("eetmeet")
	cv = ScrolledCanvas(root,600,600,600,600)
	cv.pack(side = tkinter.LEFT)
	#Here we prepre the new shapes of the game
	t = RawTurtle(cv)
	screen = t.getscreen()
	screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
	screen.register_shape("Character.gif")
	frame = tkinter.Frame(root)
	frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
	screen.tracer(10)
	sb = Spikes_bottom(cv)
	st = Spikes_top(cv)
	plr = Player(cv)
	t.goto(20,40)
	t.circle(8)
	
	# this function when it is called the game will exit    
	def quitHandler():
		root.destroy()
		root.quit()
	#here we are creating the button that you will see it on the right side of the game called Quit
    # the part it says command=quitHandler is telling the button when we click it to run the function quitHandler that we defined above
	quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
	quitButton.pack()


	# GAME LOOP (BEGIN)
	def play():
		# Tell all the elements of the game to move
		# Tell the ship to move
		plr.move()
		st.move(1)
		sb.move(2)
		if (intersect(plr,st) or intersect(plr,sb)):
			print("boom")
			quitHandler()
		# Set the timer to go off again in 5 milliseconds
		screen.ontimer(play, 5)
		# GAME LOOP (ENDS)
	# Set the timer to go off the first time in 5 milliseconds
	screen.ontimer(play,5)
	screen.onkeypress(plr.jump,"Up")
	screen.onkeypress(plr.duck, "Down")
	screen.listen()
	tkinter.mainloop()

	
if __name__ == "__main__":
	main()