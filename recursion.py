#####################################
#        Recursion Formative        #
#          Peyton Germann           #
#####################################
import turtle

t = turtle.Turtle()
end = turtle.Screen()

def recursion(len):
    if len > 0:
        t.forward(len)
        t.right(135)
        t.forward(len)
        t.left(45)
        recursion(len - 1)
recursion(150)
end.exitonclick()

    