import turtle
import time 
import random

def game():
    delay = 0.15

#Score
    score=0
    high_score=0
    bb_num = 0 

#importing the turtle library, slay
#setting up the screen
    windows = turtle.Screen()
    windows.title("Hot Chicks, Hotter Bread") #changing the title of the window 
    time.sleep(2)
    windows.bgpic("All Codes & Assets\Pei Pei\garden.gif") #changing the background picture
    windows.setup(width=800, height=700)
    windows.tracer(0) #turning off the animation, comeback to understand this later, turns off the screen updates

#creating the score
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Score:0  High Score=0",align='center',font =("Verdana",24, "normal"))

#craeting the body that moves
    body = turtle.Turtle()
    body.speed(0) #fastest animation speed
    windows.addshape("All Codes & Assets\Pei Pei\mainchick.gif")
    body.shape("All Codes & Assets\Pei Pei\mainchick.gif")
    body.penup() #makes sure that there is no line that is formed following the body 
    body.goto(0,0) #makes sure that the body starts at the origin 
    body.direction = "stop" #when it starts, it is stationery?

#creating the bread itself
    bread = turtle.Turtle()
    bread.speed(0) #fastest animation speed
    windows.addshape("All Codes & Assets\Pei Pei\hotcrossbun.gif")
    bread.shape("All Codes & Assets\Pei Pei\hotcrossbun.gif")
    bread.penup() #makes sure that there is no line that is formed following the body 
    bread.goto(0,100) #makes sure that the body starts at the origin 
#removed the body direction because the bread doesnt move but you can make it move if you need it to.

#creating the obstacles aka bad bread:
    bb= turtle.Turtle()
    bb.speed(0)
    windows.addshape("All Codes & Assets\Pei Pei\cherrybomb.gif")
    bb.shape("All Codes & Assets\Pei Pei\cherrybomb.gif")
    bb.penup()
    bb.goto(80,0)
        
    def up():
        body.direction = 'up'
    
    def down():
        body.direction = 'down'
    
    def left():
        body.direction = 'left'

    def right():
        body.direction ='right'
    
    def movement():
        if body.direction == 'up':
            y = body.ycor()
            body.sety(y+15)
            windows.addshape("All Codes & Assets\Pei Pei\_upchick.gif")
            body.shape("All Codes & Assets\Pei Pei\_upchick.gif")
            
        if body.direction == 'down':
            y = body.ycor()
            body.sety(y-15)
            windows.addshape("All Codes & Assets\Pei Pei\downchick.gif")
            body.shape("All Codes & Assets\Pei Pei\downchick.gif")
    
        if body.direction == 'left':
            x = body.xcor()
            body.setx(x-15)
            windows.addshape("All Codes & Assets\Pei Pei\leftchick.gif")
            body.shape("All Codes & Assets\Pei Pei\leftchick.gif")
        
        if body.direction == 'right':
            x = body.xcor()
            body.setx(x+15)
            windows.addshape("All Codes & Assets\Pei Pei\_rightchick.gif")
            body.shape("All Codes & Assets\Pei Pei\_rightchick.gif")
            
    windows.listen()
    windows.onkey(up, 'Up')
    windows.onkey(down, 'Down')
    windows.onkey(left, 'Left')
    windows.onkey(right, 'Right')

#main game loop
    while True:
        windows.update() #makes sure the the screen is updated.
    #okay, when you run the system at this point,the black dot will pop up for sure, but when you close the turtle tab, 
    #terminator shows up 
    
    #check collision with border 
        if body.xcor() > 290 or body.xcor() < -290 or body.ycor() >290 or body.ycor()<-290:
            time.sleep(1)
            body.goto(0,0)
            body.direction = "stop"
        
        #resetting the score to 0 once it hits the collision with the border
            score =0
            high_score=0
            pen.clear() #so that the previous score and new score dont overlap 
            pen.write("Score: {} High Score = {}".format(score,high_score),align='center', font = ("Courier",24,"normal"))
            
            windows.clearscreen()
            game()
            
        if body.distance(bb) <20:
            windows.clearscreen()
            game()
                    
    #collisions with the good bread itself
        if body.distance(bread) < 15:
            x = random.randint(-250,250)
            y = random.randint(-250,250)
            bread.goto(x,y)
            x_1 = random.randint(-300,300)
            y_1 = random.randint(-300,300)
            bb.goto(x_1,y_1)
        
        #i want to increase score and increase the number of bb as well when they win so game gets harder
            score += 1
            if score > high_score:
                high_score = score
                
            pen.clear() #so that the previous score and new score dont overlap 
            pen.write("Score: {} High Score = {}".format(score,high_score),align='center', font = ("Verdana",24,"normal"))
            
        if score ==2:
            bibi= turtle.Turtle()
            bibi.speed(0)
            windows.addshape("All Codes & Assets\Pei Pei\cherrybomb.gif")
            bibi.shape("All Codes & Assets\Pei Pei\cherrybomb.gif")
            bibi.penup()
            bibi.goto(50,50)
            
            if body.distance(bibi) < 15:
                windows.clearscreen()
                game()  
                
        if score ==3:
            bibi1= turtle.Turtle()
            bibi1.speed(0)
            windows.addshape("All Codes & Assets\Pei Pei\cherrybomb.gif")
            bibi1.shape("All Codes & Assets\Pei Pei\cherrybomb.gif")
            bibi1.penup()
            bibi1.goto(125,-201)
            
            if body.distance(bibi1) < 15:
                windows.clearscreen()
                game()  
                
        if score ==4:
            bibi2= turtle.Turtle()
            bibi2.speed(0)
            windows.addshape("All Codes & Assets\Pei Pei\cherrybomb.gif")
            bibi2.shape("All Codes & Assets\Pei Pei\cherrybomb.gif")
            bibi2.penup()
            bibi2.goto(225,40)
            
            if body.distance(bibi2) < 15:
                windows.clearscreen()
                game() 
        
        if score >= 5:
            restart = windows.textinput("You have successfully secured the bread!", "Well done, you won ! \nDo you want to restart ? (Y/N)")
            if restart == "Y":
                windows.clearscreen()
                game()
            else:
                break
        movement() #calling the move function
        time.sleep(delay) #makes sure that the body does not run off the screen too quickly
    
#makes sure that the screen is always on 
game()


# In[ ]:




