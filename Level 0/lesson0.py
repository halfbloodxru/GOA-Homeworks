from turtle import *
#we want to point a house
#step 1: draw a square 
speed (50)
width (7)
color ("purple")
begin_fill()
color ("purple")
forward(200)
left (90)

forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)
end_fill()
#end a square
#door 
forward (70)
begin_fill()
color ("brown")
left (90)
forward (100)
right (90)
forward (60)
right (90)
forward (100)
end_fill()

#roof 
penup()
goto (200, 200)
pendown()

begin_fill()
color ("orange")
right (150)
forward (200)
left (120)
forward (200)
end_fill()


#home lines
penup()
goto (0,0)
pendown()
color ("black")
right (150)
forward (200)
right (30)
forward (200)
right (120)
forward (200)
right (120)
forward (200)
penup()
goto (200,200)
pendown()
color ("black")
left (90)
forward (200)
right (90)
forward (70)
right (90)
forward (100)
left (90)
forward (60)
left (90)
forward (100)
left (90)
forward (60)
right (180)
forward (130)
#window 1 
penup()
goto(180,170)
pendown()
begin_fill()
color ("yellow")
left (90)
forward (50)
right (90)
forward (50)
right (90)
forward (50)
right (90) 
forward (50)
end_fill()
#window 2
penup()
goto(20, 170)
pendown()
begin_fill()
color ("yellow")
right (90)
forward (50)
left (90)
forward (50)
left (90)
forward (50)
left (90) 
forward (50)
end_fill()
#window 1 lines
penup()
goto(18, 172)
pendown()
width (4)
color ("black")
left (90)
forward (56)
left (90)
forward (56)
left (90)
forward (56)
left (90)
forward (56)
left (180)
forward (28)
right (90)
forward (56)
#window 2 lines
penup()
goto(182,172)
pendown()
width(4)
color ("black")
forward (56)
right (90)
forward (56)
right (90)
forward (56)
right (90)
forward (56)
right (180)
forward (28)
left(90)
forward (56)

#door handle
penup()
goto (114,55)
pendown()
width (4)
begin_fill()
circle (5)
end_fill()

penup()
goto (300,300)
pendown()


















exitonclick()