import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.pensize(4)
Eszti.color("pink")

def sokszog_rajzolas(t, n , sz):
    for i in range(8):
        t.left(-45)
        t.forward(-88)




sokszog_rajzolas(Eszti, 8, 50)

a.mainloop()
