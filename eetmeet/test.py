import turtle
t1=turtle.Turtle()

turtle.register_shape("Character.gif")
t1.shape("Character.gif")
t1.penup()
t1.goto (-350,0)
t2=turtle.Turtle()
turtle.register_shape("pizza.gif")
t2.shape("pizza.gif")
t2.penup()
t2.goto(0,250)
t2.goto(-1000,250)
turtle.mainloop()


