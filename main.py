from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading - 5)


def turn_anticlockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)


def clear_screen():
    tim.clear()
    tim.reset()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="c",fun=clear_screen)

screen.listen()
screen.exitonclick()
