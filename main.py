# Create a program that replicates the functions of the Sketch Game
import turtle
tortuga = turtle.Turtle()
screen = turtle.Screen()


def turn_up():
    """Turns turtle to face upwards"""
    tortuga.setheading(90)


def turn_down():
    """Turns turtle to face down"""
    tortuga.setheading(270)


def turn_left():
    """Turns turtle to face left"""
    tortuga.setheading(180)


def turn_right():
    """Turns turtle to face right"""
    tortuga.setheading(0)


def forwards():
    """Moves turtle forward"""
    tortuga.forward(5)


def backwards():
    """Moves turtle backwards"""
    tortuga.backward(5)


def turn_clockwise():
    """Turns turtle clockwise"""
    tortuga.right(10)


def turn_counter_clockwise():
    """Turns turtle counter clockwise"""
    tortuga.left(10)


def clear_screen():
    """Clears turtle path from the screen"""
    tortuga.clear()
    tortuga.penup()
    tortuga.home()
    tortuga.pendown()


# Allows screen to receive input
screen.listen()

# Turn keys
screen.onkey(turn_up, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_down, "Down")
screen.onkey(turn_right, "Right")
# Back and Forward Keys
screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
# Clockwise and Counter_Clockwise Keys
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(clear_screen, "c")


screen.exitonclick()
