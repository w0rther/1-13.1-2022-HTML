import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.speed(10)
Eszti.color("blue")
hossz = 2

def spiral(t,n, sz):
# t - toll; n - oldalhossz; sz - szög
    for i in [0,5,5,10]:
        t.forward(n+i)
        t.left(sz)

# első spirál
""" for i in range(1,50):
    spiral(Eszti, 10*i, 90)

a.clear() """

# második spirál

for i in range(1,50):
    spiral(Eszti, 10*i, 91)


a.mainloop()