import turtle
a = turtle.Screen()
a.bgcolor("lightgreen")
Sanyi = turtle.Turtle()
Sanyi.pensize(4)
Sanyi.color("pink")
def negyzetek(t, h):
   for i in range(4):
      t.forward(h)
      t.left(90)



meret=20
for j in range(5):
   negyzetek(Sanyi,meret)
   meret = meret+20
   Sanyi.penup()
   Sanyi.goto(Sanyi.xcor()-10, Sanyi.ycor()-10)
   Sanyi.pendown()


a.mainloop()