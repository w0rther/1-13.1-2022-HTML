import turtle
a = turtle.Screen()
Eszti = turtle.Turtle()

def csillag(t, sz , n):
   for i in range(5):
      t.forward(n)
      t.left(sz)

csillag(Eszti, 144, 100)

a.mainloop()