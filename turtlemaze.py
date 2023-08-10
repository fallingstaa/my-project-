import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Maze")

# Draw the maze
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(-200, 200)
pen.pendown()
pen.pensize(5)
for i in range(4):
    pen.forward(400)
    pen.right(90)
pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the goal turtle
goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.speed(0)
x = random.randint(-180, 180)
y = random.randint(-180, 180)
goal.goto(x, y)

# Create the score turtle
score = turtle.Turtle()
score.hideturtle()
score.speed(0)
score.penup()
score.goto(0, 260)

# Set the initial score
score_value = 0
score.write("Score: {}".format(score_value), align="center", font=("Courier", 24, "normal"))

# Function to update the score
def update_score():
    global score_value
    score_value += 1
    score.clear()
    score.write("Score: {}".format(score_value), align="center", font=("Courier", 24, "normal"))
    if score_value >= 10:
        player.hideturtle()
        goal.hideturtle()
        score.goto(0, 0)
        score.write("Winner!", align="center", font=("Courier", 24, "normal"))

# Function to show the error message
def show_error():
    player.hideturtle()
    goal.hideturtle()
    score.goto(0, 0)
    score.write("Lost!", align="center", font=("Courier", 24, "normal"))

# Set the movement functions
def move_up():
    player.setheading(90)
    player.forward(10)
    if player.ycor() > 190 or player.ycor() < -190:
        show_error()
def move_down():
    player.setheading(270)
    player.forward(10)
    if player.ycor() > 190 or player.ycor() < -190:
        show_error()
def move_left():
    player.setheading(180)
    player.forward(10)
    if player.xcor() > 190 or player.xcor() < -190:
        show_error()
def move_right():
    player.setheading(0)
    player.forward(10)
    if player.xcor() > 190 or player.xcor() < -190:
        show_error()

# Set the keyboard bindings
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
while True:
    # Check if the player has reached the goal
    if player.distance(goal) < 20:
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        goal.goto(x, y)
        update_score()
    
    # Check for collision with walls and corners
    if player.xcor() > 190 or player.xcor() < -190 or player.ycor() > 190 or player.ycor() < -190:
        show_error()
    
    # Update the screen
    wn.update()