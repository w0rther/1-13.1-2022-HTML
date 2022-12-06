import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Eszti = turtle.Turtle()


def sokszog_rajzolas (t, n, sz):
    for i in range(sz):
        t.left(180-(sz-2)*180/sz)
        t.forward(n)

def szabalyos_haromszog_rajzolas(t, sz):
    sokszog_rajzolas(t, 100, sz)


szabalyos_haromszog_rajzolas(Eszti, 3)


a.mainloop()

