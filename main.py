import turtle


drawing_board = turtle.Screen()
drawing_board.bgcolor("lightblue")
drawing_board.title("Python Turtle")

#square
turtle_instance = turtle.Turtle()
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(90)
turtle_instance_2.forward(100)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance_2.right(90)
turtle_instance_2.forward(100)

#star
turtle_instance =turtle.Turtle()
for i in range(5):
    turtle_instance.forward(200)
    turtle_instance.left(144)



#polygon
turtle_instance = turtle.Turtle()

numberofsides = 12
angle = 360 / numberofsides
side_length = 50

for i in range(numberofsides):
    turtle_instance.forward(side_length)
    turtle_instance.left(angle)

turtle.done()
