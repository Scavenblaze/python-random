import turtle
import winsound

# window
wn = turtle.Screen()
wn.title("pong game made by the greatest programmer in this world, now with soundsss")
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.tracer(0)

# paddle a
pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(5,1)
pa.penup()
pa.goto(-350, 0)

# paddle b
pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(5,1)
pb.penup()
pb.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.09 #moves by 2 pixel
ball.dy=0.09 #so x and y makes it go diagonally
# okay nvm 2,1,0.5 was too fast for my pc... 0.1 was smooth but kinda fast for a pong game yk... 0.05 feels too slow for some reason
# note increase/reduce dx, dy value if ball is too slow/fast

# move paddle
def pa_up():
    y = pa.ycor()
    if(y<250):
        y += 20  # moves paddle up
        pa.sety(y)
    wn.update()

def pa_down():
    y = pa.ycor()
    if(y>-250):
        y -= 20  # moves paddle down
        pa.sety(y)
    wn.update()

def pb_up():
    y = pb.ycor()
    if(y<250):
        y += 20  # moves paddle up
        pb.sety(y)
    wn.update()

def pb_down():
    y = pb.ycor()
    if(y>-250):
        y -= 20  # moves paddle down
        pb.sety(y)
    wn.update()

#scoring
score_a=0
score_b=0


#draw score
draw= turtle.Turtle()
draw.speed(0)
draw.color("yellow")
draw.penup()     #does not draw
draw.hideturtle()    #hides thingy
draw.goto(0, 260)
draw.write("Player 1: {}\t Player 2: {}".format(score_a, score_b), align="center", font=("Monospace", 20, "normal"))


# inputs
wn.listen()  # listens
wn.onkeypress(pa_up, "w")
wn.onkeypress(pa_down, "s")
wn.onkeypress(pb_up, "Up")
wn.onkeypress(pb_down, "Down")



#main loop
while True:
    wn.update()
    
    #moving ball
    ball.setx(ball.xcor() + ball.dx) #gets initial pos and adds x
    ball.sety(ball.ycor() + ball.dy)
    
    #border check... note window height is 600 so 300+300... ball is some pixel big so trial and error this
    if ball.ycor()>290:     #for top
        ball.sety(290)
        ball.dy*=-1
        
        
    if ball.ycor()<-290:     #for bottom
        ball.sety(-290)
        ball.dy*=-1
        
        
    if ball.xcor()>390:     #for rside
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        draw.clear()
        draw.write("Player 1: {}\t Player 2: {}".format(score_a, score_b), align="center", font=("Monospace", 20, "normal"))
        winsound.PlaySound("pong/pong_win1.wav", winsound.SND_ASYNC)
        
    if ball.xcor()<-390:    #for lside
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        draw.clear()
        draw.write("Player 1: {}\t Player 2: {}".format(score_a, score_b), align="center", font=("Monospace", 20, "normal"))
        winsound.PlaySound("pong/pong_win1.wav", winsound.SND_ASYNC)
        
    #ball paddle coll... note paddle is x 350, 10 wide and 50 height
    if ball.xcor()>340 and ball.xcor() < 350 and (ball.ycor()<pb.ycor()+40 and ball.ycor()>pb.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong/paddle_hit1.wav", winsound.SND_ASYNC)
        #SND_ASYNC prevents program to stop after playing sound
    
    if ball.xcor()<-340 and ball.xcor() > -350 and (ball.ycor()<pa.ycor()+40 and ball.ycor()>pa.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong/paddle_hit1.wav", winsound.SND_ASYNC)  