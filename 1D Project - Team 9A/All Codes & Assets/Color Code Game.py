#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
import random

screen=turtle.Screen()
screen.mode('standard')
screen.setup(1000,700)
screen.tracer()

speed=0.3 #used in later draw function
n=4 #number of colors in nth numbered code, increases with increasing difficulty
colors=['yellow','green','blue','purple','pink','red','black','brown'] #choose n colors for code
code=[] #empty list for computer's code

#set code
for i in range(0,n):
    pin=random.choice(colors) #generates random colors for code
    code.append(pin) #adds color to code list

#draws circles in code/guess
def draw(color,radius,x,y):
    dis=turtle.Turtle()
    dis.hideturtle()
    turtle.delay(50) #pause before drawing
    dis.penup()
    dis.goto(x,y)
    dis.pendown()
    dis.speed(speed)
    dis.showturtle()
    dis.shape('circle')
    dis.color(color)
    dis.shapesize(radius)
    dis.hideturtle()
    dis.penup()

#event that flashes computer's code for player to rmb
def play():
    for i in code:
        x=random.randint(-300,300)
        y=random.randint(-250,250)
        rad=random.randint(2,15) 
        draw(i,rad,x,y) #x,y,radius of circle rad are random

#txtbox for instructions, feedback at top of the screen
def draw_txtbox():
    box= turtle.Turtle()
    box.hideturtle()
    box.penup()
    box.setpos(10, 300)
    box.pendown()
    box.speed(0)
    box.showturtle()
    box.shape("square")
    box.shapesize(stretch_wid=5, stretch_len=80)
    box.color("white")
    box.penup()

#shows instructions, feedback at top of the screen, used w draw_txtbox()
def write(text,x,y,fsize):
    word=turtle.Turtle() 
    word.hideturtle()
    word.penup()
    word.goto(x,y)
    word.showturtle()
    word.pendown()
    word.write(text,font=("Courier",fsize,"normal"))

#shows player's guess
def show_guess(color,radius,x,y):
    guess=turtle.Turtle()
    guess.penup()
    guess.goto(x,y)
    guess.pendown()
    guess.speed(0.5)
    guess.shape('circle')
    guess.color(color)
    guess.shapesize(radius)
    guess.penup()

## ACTION STARTS HERE
write('BROWN-PINK-BEIGE-PURPLE, four colors will flash in order',-350,290,15)
write('YELLOW-BLUE-RED-GREEN, remember the pattern and select colors to win!',-385,270,15)      

#plays computer's code
play()

#creates color bar that players can select colors from
ls=[] #empty list for player's guess
class Color:
    def __init__(self,color,x,y):
        self.color = turtle.Turtle()
        self.color.speed(0)
        self.color.setpos(x,y) #y constant, x decreasing to form one row of colors        
        self.color.penup()
        self.color.pendown()
        self.color.speed(0)        
        self.color.shape("circle") 
        self.color.speed(0)        
        self.color.shapesize(2)
        self.color.color(color) #black outline, colored fill
        self.color.onclick(self.click) #responds to player's clicks
        self.coloratt=color #color of circle
        

    def click(self,x,y): #after player clicks,the following happens...
        spaces_filled=len(ls)
        print(spaces_filled,'g')
        if spaces_filled<n: #ensures all n spaces in code are filled, if not player shld continue clicking on colors
            ls.append(self.coloratt) #adds current color to player's guess
            spaces_filled+=1 #updates no of colors in list
            print(ls)
            print(code)
        else:
            for i in ls:
                show_guess(i,5,0,0) #shows player's guess color by color
            print(ls,code)
            if ls==code: #checks if player's guess==code
                draw_txtbox()
                write('Congrats Chick, you guessed the code!',-320,260,25)
            else:
                print(ls,'end turn')
                ls.clear()
                draw_txtbox()
                write('GUESS again!',-100,260,25)
                play()
        return

all_colors=['yellow','green','blue','purple','pink','red','black','brown','beige']
write('choose four colors',-400,-230,15)
for color in all_colors:
    x=-(110+35*all_colors.index(color)) #sets x-coord for color
    y=-250 #sets y-coord for color
    Color(color,x,y)



turtle.done()


# In[ ]:




