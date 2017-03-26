import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle,linelen):
    if linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        drawSpiral(myTurtle,linelen-5)

#drawSpiral(myTurtle,100)
#myWin.exitonclick()

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(40)
        tree(branchLen-10,t)
        t.left(80)
        tree(branchLen-10,t)
        t.right(40)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
main()
