import turtle

wn = turtle.Screen() #Create a screen
wn.title("Pong by @Spandan")
wn.bgcolor("black") #Classic pong game color
wn.setup(width=800, height=600)
wn.tracer(0) #Stops the window from updating. Speed up our games a bit

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
