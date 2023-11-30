import turtle
import winsound

# Main Screen
win = turtle.Screen()
win.title("Jumping Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Platform
ground = turtle.Turtle()
ground.shape("square")
ground.shapesize(stretch_wid=1, stretch_len=40)
ground.color("white")
ground.penup()
ground.goto(0, -100)

# Player
player = turtle.Turtle()
player.shape("circle")
player.speed(0)
player.shapesize(stretch_wid=1, stretch_len=1)
player.color("white")
player.penup()
player.goto(-350, -80)

# Moving Object
obj = turtle.Turtle()
obj.shape("square")
obj.speed(0)
obj.shapesize(stretch_wid=2, stretch_len=1)
obj.color("white")
obj.penup()
obj.goto(350, -80)

# Promt
promt = turtle.Turtle()
promt.speed(0)
promt.color("white")
promt.penup()
promt.hideturtle()
promt.goto(0, 260)
promt.write("Press 'SPACEBAR' to jump", align = "center", font = ("Courier", 24, "normal"))

# Scoreboard 
score_a = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 230)
score.write("Score : 0",align = "center", font = ("Courier", 24, "normal"))


# Player Jump Height
def player_jump():
    y = player.ycor()
    y += 80
    player.sety(y)
    winsound.PlaySound("./sounds/boink.wav", winsound.SND_ASYNC)


# Gravity Speed
player.dy = 0.20
obj.dx = 0.20

# Keyboard Bindings
win.listen()
win.onkeypress(player_jump, "space")

# Main game loop
while True:
    win.update()

    # Player Gravity
    player.sety(player.ycor() - player.dy)

    # Objetc Collision
    if (obj.xcor() < -340 and obj.xcor() >-350) and (obj.ycor() < player.ycor() + 40 and obj.ycor() > player.ycor() -40):
        obj.dx *= 0
        score.clear()
        promt.clear()
        score.goto(0, 50)
        score.write("Game Over Your Score : {}".format (score_a) , align = "center", font = ("Courier", 20, "normal"))

    # Object Move
    obj.setx(obj.xcor() - obj.dx)
    if (obj.xcor() <= -400):
        obj.setx(350)
        obj.dx += 0.02
        score_a += 1
        score.goto(0, 230)
        score.clear()
        score.write("Score : {}".format (score_a) , align = "center", font = ("Courier", 24, "normal"))

    # Player Bounce
    if (player.ycor() <= -80):
        player.sety(-80)
        player.dy == -1

