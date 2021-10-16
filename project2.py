#Cole Hill
#CPSC 1301
#Febuary 7, 2020
#Project 2

#get turtle
import turtle

#open turtle window
wn=turtle.Screen()

#set background color
wn.bgcolor("black")
#name turtle
cole=turtle.Turtle()

#get turtle in position
cole.goto(-100,0)
#set pen color
cole.color("red")

#set pen size
cole.pensize(25)

#set turtle speed
cole.speed(3)


#make a C

cole.left(135)
for i in[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
    cole.forward(15)
    cole.left(15)
    cole.forward(15)

#pick pen up
cole.up()

#move pen
cole.right(45)
cole.forward(60)

#put pen down
cole.down()

#change pen color
cole.color("green")

#change pensize
cole.pensize(25)

#make a R
cole.left(90)
cole.forward(175)
cole.right(90)
cole.forward(75)
cole.right(15)
cole.forward(25)
cole.right(45)
cole.forward(25)
cole.right(60)
cole.forward(50)
cole.right(60)
cole.forward(70)
cole.right(225)
cole.forward(150)
                
            
#pick pen up
cole.up()

#place pen
cole.left(45)
cole.forward(100)
#put pen down
cole.down()

#change pen color
cole.color("yellow")

#change pen size
cole.pensize(25)


# make a H
cole.left(90)
cole.forward(200)
cole.left(180)
cole.forward(100)
cole.left(90)
cole.forward(100)
cole.left(90)
cole.forward(100)
cole.right(180)
cole.forward(200)



#set exit on click
wn.exitonclick()
