import turtle

wn = turtle.Screen() #Create a screen
wn.title("Pong by @Spandan")
wn.bgcolor("black") #Classic pong game color
wn.setup(width=800, height=600)
wn.tracer(0) #Stops the window from updating. Speed up our games a bit

#Main game loop - Every game has it
while True:
    wn.update()
