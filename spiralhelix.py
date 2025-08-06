import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Sprial Helix")
turtle.speed(0)
turtle_color = ["blue","white","cyan","yellow","green","darkblue","brown","purple","red"]

turtle_instance = turtle.Turtle()

for i in range(30):
    turtle_instance.color(turtle_color[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.right(30)