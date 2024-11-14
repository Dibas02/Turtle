import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)

a = turtle.Turtle()

for i in range(6):
    turtle.forward(100)
    turtle.right(60)

turtle.mainloop()
turtle.done()
