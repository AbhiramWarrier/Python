import turtle
Screen = turtle.Screen()
turtle.Screen().bgcolor("red")
Screen.setup(width=600, height=600)

t = turtle.Turtle
board = turtle.Turtle()



board.penup()


board.pendown()

for i in range(20):
    board.circle(i * 10)
    

turtle.done()