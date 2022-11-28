import turtle
a = turtle.Screen()
Eszti = turtle.Turtle()
a.bgcolor("lightgreen")
Eszti.pensize(4)
Eszti.color("pink")

Eszti.left(35)
for i in range(0,5):
   Eszti.forward(100)
   Eszti.left(144)

a.mainloop()