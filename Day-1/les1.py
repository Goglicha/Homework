from turtle import*
speed(20)
width(7)
color("green")

#square
begin_fill()
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90) 
end_fill()

#door
begin_fill()
forward(110)
color("blue")
left(90)
forward(120)
right(90)
forward(80)
right(90)
forward(120)
end_fill()

#roof

penup()
goto(300,300)
pendown()

begin_fill()
color("yellow")
right(150)
forward(300)
left(120)
forward(300)
end_fill()

#window-1

penup()
goto(35,180)
pendown()
begin_fill()
color("red")
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


#window-2

penup()
goto(265,180)
pendown()
begin_fill()
color("red")
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

width(3)
color("black")
penup()
goto(60,230)
pendown()
forward(50)


penup()
goto(35,205)
pendown()
left(90)
forward(50)

penup()
goto(240,230)
pendown()
right(90)
forward(50)

penup()
goto(265,205)
pendown()
right(90)
forward(50)




exitonclick()



