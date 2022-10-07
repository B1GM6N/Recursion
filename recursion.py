#####################################
#        Recursion Formative        #
#          Peyton Germann           #
#####################################
import turtle
# adds turtle
t = turtle.Turtle()
end = turtle.Screen()
# function that draws a star
# calls itself over and over again till
# the length is 0
def recursion(len):
    if len > 0:
        t.forward(len)
        t.right(135)
        t.forward(len)
        t.left(45)
        recursion(len - 1)
recursion(150)
# makes turtle exit when you click it
end.exitonclick()