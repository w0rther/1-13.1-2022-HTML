import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.pensize(4)
Eszti.color("pink")
Eszti.speed(15)

def minta(t,h):
    for i in range(4):
        t.forward(h)
        t.left(90)


for j in range(24):
    minta(Eszti,200)
    Eszti.left(15)
    

a.mainloop()


    
