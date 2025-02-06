from turtle import *


# we want to paint a house

#step 1: draw a square
speed(8)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of scuare

#drawing a door


forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)   #hright of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#step 2: draw a window


penup()
goto(10, 100)
pendown()
color("brown")
begin_fill()
left(120)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()





# step 3: draw anather window




penup()
goto(135, 100)
pendown()
color("brown")
begin_fill()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

exitonclick()