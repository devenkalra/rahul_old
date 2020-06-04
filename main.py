from graphics import *

def hello():
    print ("hello!")


win = GraphWin("My Circle", 300, 100)

c = Circle(Point(50,50), 10)
#c.draw(win)


for x in range(0, 100, 4):
    r = Rectangle(Point(0, 0), Point(100, 100))
    r.setFill("white")
    r.setOutline("white")
    r.draw(win)
    c = Circle(Point(x, 50), 10)
    c.setOutline("black")
    c.setWidth(3)
    c.draw(win)
    time.sleep(0.1)

for y in range(0, 100, 4):
    c = Circle(Point(50, y), 10)
#     c.draw(win)
win.getMouse() # Pause to view result
win.close()    # Close window when done

