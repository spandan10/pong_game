import turtle
import time

wn = turtle.Screen() #Create a screen
wn.title("Pong by @Spandan")
wn.bgcolor("black") #Classic pong game color
wn.setup(width=800, height=600)
wn.tracer(0) #Stops the window from updating. Speed up our games a bit

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of the animation. Sets the speed of the maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #Turtle draws a line which we do not want
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of the animation. Sets the speed of the maximum possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #Turtle draws a line which we do not want
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #Speed of the animation. Sets the speed of the maximum possible speed
ball.shape("square")
ball.color("white")
ball.penup() #Turtle draws a line which we do not want
ball.goto(0,0)

ball.dx = 0.2 # ball movement in x-axis by 2 pixels
ball.dy = -0.2 # ball movement in y-axis by 2 pixels

# Pen
pen = turtle.Turtle()
pen.speed(0) # Animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_a_up():
    y = paddle_a.ycor() #Returns the y-coordinate and assigns it to y variable
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #Returns the y-coordinate and assigns it to y variable
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #Returns the y-coordinate and assigns it to y variable
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #Returns the y-coordinate and assigns it to y variable
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen() #Listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #When the user presses w, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down")

#Main game loop - Every game has it
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
    
    if ball.xcor() > 390:
        ball.goto(0,0) #Since, the ball will go out of the game. It should come to the centre
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0) #Since, the ball will go out of the game. It should come to the centre
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))        
    
    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1
