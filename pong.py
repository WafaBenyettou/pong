import turtle

wn = turtle.Screen()
# the window
wn.title("Pong by freecodecamp")
# the title
wn.bgcolor("black")
# background color
wn.setup(width=800, height=600)
# sizing
wn.tracer(0)

# wn.tracer stops the window from updating so we have mainually to update it
# so its speed up the game a little bit

# Score
score_a=0
score_b=0










# add the ball and paddles to the screen

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed()
# the speed of animation, this is just smthg we need for the turtle module
# it sets the speed to the max speed otherwise things  would be really slow
paddle_a.shape("square")
#shape of the paddle by default 20px by 20px
paddle_a.color("white")
#paddle color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#stretch the shape
paddle_a.penup()
#cz turtle by def draw a line as they are moving
#and we dont need to draw lines so we do the penup
paddle_a.goto(-350,0)
#want my paddle to start at -350 cord X and 0 and vertically centred in the screen

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)


# Ball

Ball = turtle.Turtle()
Ball.speed()
Ball.shape("circle")
Ball.color("red")
Ball.penup()
Ball.goto(0,0)
# separate the ball mov in 2 parts (x mov and y mov)
Ball.dx = 0.8
Ball.dy = -0.8



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0 Player B : 0", align="center", font=("Courier",24,"normal"))

# functions to move the paddles up and down
def paddle_a_up():
      y = paddle_a.ycor()
      # y.cor returns the y coordinates
      y +=20
      # that will add 20px to the cord
      paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding

wn.listen()
# listen for keyboard input
wn.onkeypress(paddle_a_up,"z")
# when the user presses z call the function paddle a up
wn.onkeypress(paddle_a_down,"w")
# when the user presses w call the function paddle a down
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")







# main game loop
while True:
    wn.update()
    # every time the loop runs it update the screen

    # move the ball
    Ball.setx(Ball.xcor()+ Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() >390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (Ball.xcor() > 340 and Ball.xcor()<350) and (Ball.ycor()<paddle_b.ycor() +40 and Ball.ycor() > paddle_b.ycor() -40) :
        Ball.setx(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor()>-350) and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1
