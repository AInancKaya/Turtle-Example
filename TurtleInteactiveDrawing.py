import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Interactive Drawing")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(30)
def turtle_angle_left():
    turtle_instance.setheading(turtle_instance.heading() + 30)
def turtle_angle_right():
    turtle_instance.setheading(turtle_instance.heading() - 30)
def screen_clear():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="w")
drawing_board.onkey(fun=turtle_angle_left, key="a")
drawing_board.onkey(fun=turtle_angle_right, key="d")
drawing_board.onkey(fun=screen_clear, key="c")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="Up")
drawing_board.onkey(fun=turtle_pen_down, key="Down")


turtle.mainloop()
