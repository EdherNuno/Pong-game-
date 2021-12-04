"""
This was made by followin  a tutorial by @TokyoEdTech.
Toririal on youtube @ freeCodeCamp "Learn python by building games - Full Course"
"""
import turtle
import random

wn = turtle.Screen()        #Create a window
wn.title("Pong Game")       #Window title
wn.bgcolor("black")         #Window background color
wn.setup(width=800,         #Window size
         height=600)
wn.tracer(0)                #set window update as manual to increase speed, in this tutorial

#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()  #turtle object (first turtle refears to the module, secon Turtle refears to the class within the module)
paddle_a.speed(0)           #speed animation , 0 is the maximum
paddle_a.shape("square")    #set a the paddle to be a square 20x20 pixels
paddle_a.shapesize(stretch_wid=5, stretch_len=1)   #paddle wid multiply by 5 making it 100x20 pixels
paddle_a.color("white")
paddle_a.penup()            #check behavior without this line
paddle_a.goto(-350,0)       #paddle appears @ -350x , 0y (0 is @ center of the window)




#Paddle B
paddle_b = turtle.Turtle()  #turtle object (first turtle refears to the module, secon Turtle refears to the class within the module)
paddle_b.speed(0)           #speed animation , 0 is the maximum
paddle_b.shape("square")    #set a the paddle to be a square 20x20 pixels
paddle_b.shapesize(stretch_wid=5, stretch_len=1)   #paddle wid multiply by 5 making it 100x20 pixels
paddle_b.color("white")
paddle_b.penup()            #check behavior without this line
paddle_b.goto(350,0)       #paddle appears @ 350x , 0y



#Ball
ball = turtle.Turtle()  #turtle object (first turtle refears to the module, secon Turtle refears to the class within the module)
ball.speed(0)           #speed animation , 0 is the maximum
ball.shape("square")    #set a the paddle to be a square 20x20 pixels
ball.color("white")
ball.penup()            #check behavior without this line
ball.goto(0,0)       #paddle appears @ 350x , 0y
#For the ball movement is convinient to separete into x_mov and y_mov
ball.dx = 0.05
ball.dy = -0.05

#Pen
pen = turtle.Turtle()
pen.speed(0)
#pen.shape("line")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#pen.write("Player_A: "+ str(score_a) + " Player_B: 0", align = "center", font = ("Courier",24,"normal"))
pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align = "center", font = ("Courier",24,"normal"))

#funtions

def paddle_a_up():
    """ Move the left paddle up when w key is press.
    Checks if paddle has reach the top of the window"""
    y = paddle_a.ycor()     #return the y coordinate for the object paddle_a
    if y <= 250:
        y += 20                 #calculate new y position. Each  call of function add 20 pixels to paddle position
        paddle_a.sety(y)        #set paddle position to the new calculated coordinate

def paddle_a_down():
    """ Move the left paddle down when s  key is press.
    Checks if paddle has reach the top of the window"""
    y = paddle_a.ycor()     #return the y coordinate for the object paddle_a
    if y >= -250:
        y -= 20                 #calculate new y position. Each  call of function add 20 pixels to paddle position
        paddle_a.sety(y)        #set paddle position to the new calculated coordinate

def paddle_b_up():
    """ Move the left paddle up when w key is press.
    Checks if paddle has reach the top of the window"""
    y = paddle_b.ycor()     #return the y coordinate for the object paddle_b
    if y <= 250:
        y += 20                 #calculate new y position. Each  call of function add 20 pixels to paddle position
        paddle_b.sety(y)        #set paddle position to the new calculated coordinate

def paddle_b_down():
    """ Move the left paddle down when s  key is press.
    Checks if paddle has reach the top of the window"""
    y = paddle_b.ycor()     #return the y coordinate for the object paddle_b
    if y >= -250:
        y -= 20                 #calculate new y position. Each  call of function add 20 pixels to paddle position
        paddle_b.sety(y)        #set paddle position to the new calculated coordinate




#keyboard binding
wn.listen()             #set the window to "listen to the keyboard"
wn.onkeypress(
              paddle_a_up,  #call the function
              "w"           #key to listen
             )
wn.onkeypress(paddle_a_down, "s") #move paddle down
wn.onkeypress(paddle_b_up, "o") #move paddle down
wn.onkeypress(paddle_b_down, "l") #move paddle down



#Main geme loop
while True:
    wn.update()             #update the windows with each loop

    #Move the ball
#    ball.dx = random.uniform(0.05,0.5)
#    ball.dy = random.uniform(0.05,0.5)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border checking

    #Bounde from top edge
    if ball.ycor() > 290:           #check if ball pos is less than 300 (the ball itsaelf is 20x20) if not keep going up
        ball.sety(290)              #sanity check
        ball.dy *= -1               #set delta y to negative to revese direction

    #bounce from bottom edge
    if ball.ycor() < -290:           #check if ball pos is less than 300 (the ball itsaelf is 20x20) if not keep going up
        ball.sety(-290)              #sanity check
        ball.dy *= -1               #set delta y to negative to revese direction

    #pass from right edge
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align = "center", font = ("Courier",24,"normal"))


    #bounce from left edge
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player_A: {}   Player_B: {}".format(score_a, score_b), align = "center", font = ("Courier",24,"normal"))

    #ball collision on paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor()  > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
